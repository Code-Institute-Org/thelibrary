from slugify import slugify
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

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


