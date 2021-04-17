from slugify import slugify
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
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


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'body']

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


def deactivate_post(request, pk):
    """ Changes status of a post to deactivated """
    post = get_object_or_404(Post, pk=pk)
    post.status = 'Deactivated'
    post.save()

    return redirect('review_posts')


class ReviewPostView(DetailView, UpdateView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    fields = ['mod_message']

    def form_valid(self, form):
        form.instance.moderator = self.request.user
        return super().form_valid(form)