from slugify import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from users.models import User, UserProfile
from .forms import FlagForm
from .models import Post, PostCategory, PostFlag


class AllPostsView(ListView):
    """ Basic view to see all posts """
    template_name = 'all_posts.html'
    paginate_by = 4
    queryset = Post.objects.filter(status='Approved').order_by('-created_on')
    context_object_name = 'posts'


class PostDetailView(DetailView, SuccessMessageMixin):
    """ Create view for full post """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    success_message = "Thank you for flagging this post, an admin will review it shortly"

    def get_context_data(self, *args, **kwargs):

        context = super(
            PostDetailView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        context['total_likes'] = post.total_likes()
        context['liked'] = post.likes.filter(
            id=self.request.user.id).exists()
        context['bookmarked'] = post.bookmarks.filter(
            id=self.request.user.id).exists()
        # instead of sending total_posts, instead create a method of UserProfile
        # that returns the badge type based on the number of posts
        # this can then be used to control the kudos badge
        context['total_posts'] = post.author.total_posts()
        context['form'] = FlagForm()

        return context

    def post(self, request, *args, **kwargs):
        form = FlagForm(request.POST)
        if form.is_valid():
            # Add flagger details to PostFlag instance
            form.instance.flagger = get_object_or_404(
                User, pk=self.request.user.pk
            ) 
            form.save()

            # Attach PostFlag instance to relevant Post
            post = get_object_or_404(Post, id=self.kwargs['pk'])
            post.flag = get_object_or_404(PostFlag, pk=form.instance.pk)
            post.save()

            # Create context, set success message and render
            self.object = self.get_object()
            context = super(PostDetailView, self).get_context_data(**kwargs)
            context['form'] = FlagForm
            messages.success(self.request, self.success_message)
            return self.render_to_response(context=context)

        else:
            self.object = self.get_object()
            context = super(PostDetailView, self).get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)

    def get_success_url(self):
        return reverse(
        'detail_view',
        kwargs={
            'pk': self.object.pk,
            'slug': self.object.slug 
        })

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = [
        'title',
        'summary',
        'image_1',
        'image_2',
        'image_3',
        'image_4',
        'body',
        'category',
        'tags'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('review_post', kwargs={'pk': self.object.pk})


class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    context_object_name = 'post'
    fields = [
        'title',
        'summary',
        'image_1',
        'image_2',
        'image_3',
        'image_4',
        'body',
        'category',
        'tags'
    ]

    def form_valid(self, form):
        if form.instance.status == 'Review':
            form.instance.status = 'Waiting'
        form.instance.updated_on = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        if self.object.status == 'Waiting':
            return reverse('review_post', kwargs={'pk': self.object.pk, 'slug': self.object.slug })
        else:
            return reverse('post_detail', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class ReviewPostsView(LoginRequiredMixin, ListView):
    template_name = 'review_posts.html'
    paginate_by = 4
    queryset = Post.objects.filter(status='Waiting').order_by('-created_on')
    context_object_name = 'posts'

    def get(self, *args, **kwargs):
        user = self.request.user
        if user.userprofile.is_mod == False:
            return redirect('home')
        return super(ReviewPostsView, self).get(*args, **kwargs)


def approve_post(request, pk, slug):
    """
    Changes status of a post to approved if the user accessing the url
    is a moderator. Of not, user is redirected to home page.
    """
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user and request.user.userprofile.is_mod:
        post.status = 'Approved'
        post.save()
        return redirect('review_posts')
    else:
        return redirect('home')


def delete_post(request, pk):
    """ Deletes post """
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()

        # Change this to redirect to where user was 
        # looking before the post they deleted?
        return redirect('home')
    
    # redirect users who are not the author away from
    # delete url without deleting post
    else:
        return redirect('home')


class ReviewPostView(DetailView, UpdateView):
    model = Post
    template_name = 'post_review.html'
    context_object_name = 'post'
    fields = ['mod_message']

    def get(self, *args, **kwargs):
        user = self.request.user
        if user.userprofile.is_mod == False:
            return redirect('home')
        return super(ReviewPostView, self).get(*args, **kwargs)

    def form_valid(self, form):
        form.instance.moderator = self.request.user
        form.instance.status = 'Review'
        return super().form_valid(form)


class CategoryView(SingleObjectMixin, ListView):
    paginate_by = 4
    template_name = 'category.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=PostCategory.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        return context

    def get_queryset(self):
        return self.object.post_category.all()


class AuthorPostsView(SingleObjectMixin, ListView):
    paginate_by = 4
    template_name = 'post_by_author.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.object
        return context

    def get_queryset(self):
        return self.object.userprofile.posts.all()
    

def like_post(request, pk):
    """ Adds like to post, tied to specific user """
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[pk, post.slug]))


def bookmark_post(request, pk):
    """ Adds post to users bookmarks """
    post = get_object_or_404(Post, pk=pk)

    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[pk, post.slug]))


