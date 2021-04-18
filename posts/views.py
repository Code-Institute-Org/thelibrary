from slugify import slugify
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from users.models import User

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
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'category', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class ReviewPostsView(LoginRequiredMixin, ListView):
    template_name = 'review_posts.html'
    # ~Q is used to negate a specific status,
    # results in getting all items that don't have the 'Approved' status
    queryset = Post.objects.filter(~Q(status='Approved')).order_by('-created_on')
    context_object_name = 'posts'

    def get(self, *args, **kwargs):
        user = self.request.user
        if user.userprofile.is_mod == False:
            return redirect('home')
        return super(ReviewPostsView, self).get(*args, **kwargs)


def approve_post(request, pk):
    """ Changes status of a post to approved """
    post = get_object_or_404(Post, pk=pk)
    post.status = 'Approved'
    post.save()

    return redirect('review_posts')


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
    template_name = 'post_detail.html'
    context_object_name = 'post'
    fields = ['mod_message']

    def form_valid(self, form):
        form.instance.moderator = self.request.user
        form.instance.status = 'Review'
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    context_object_name = 'post'
    fields = ['title', 'category', 'body']

    def form_valid(self, form):
        if form.instance.status == 'Review':
            form.instance.status = 'Waiting'
        return super().form_valid(form)


def like_post(request, pk):
    """ Adds like to post, tied to specific user """
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[pk, post.slug]))

