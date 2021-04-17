from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post
# Create your views here.


class AllPostsView(ListView):
    """ Basic view to see all posts """
    template_name = 'all_posts.html'
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(status='Approved').order_by('-created_on')
    context_object_name = 'posts'

class PostDetailView(DetailView):
    """ Create view for full post """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'