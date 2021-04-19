from slugify import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, PostCategory
from users.models import User, UserProfile

# Create your views here.


class AllPostsView(ListView):
    """ Basic view to see all posts """
    template_name = 'all_posts.html'
    queryset = Post.objects.filter(status='Approved').order_by('-created_on')
    context_object_name = 'posts'

class PostDetailView(DetailView):
    """ Create view for full post """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        context['total_likes'] = post.total_likes()
        context['liked'] = post.likes.filter(id=self.request.user.id).exists()
        context['bookmarked'] = self.request.user.userprofile.bookmarks.filter(id=post.id).exists()
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'summary', 'body', 'category', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    context_object_name = 'post'
    fields = ['title', 'summary', 'body', 'category', 'tags']

    def form_valid(self, form):
        if form.instance.status == 'Review':
            form.instance.status = 'Waiting'
        form.instance.updated_on = timezone.now()
        return super().form_valid(form)


class ReviewPostsView(LoginRequiredMixin, ListView):
    template_name = 'review_posts.html'
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

    def form_valid(self, form):
        form.instance.moderator = self.request.user
        form.instance.status = 'Review'
        return super().form_valid(form)


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
    user_profile = get_object_or_404(UserProfile, pk=request.user.id)
    bookmarks = user_profile.bookmarks.all()

    if post in bookmarks:
        user_profile.bookmarks.remove(post)
    else:
        user_profile.bookmarks.add(post)

    return HttpResponseRedirect(reverse('post_detail', args=[pk, post.slug]))


def category_view(request, pk, category):

    posts = Post.objects.filter(category=pk).order_by('-created_on')
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'category.html', context)