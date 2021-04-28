from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from posts.models import Post, PostCategory


# Create your views here.
@login_required
def home_view(request):
    """
    Render home page with 5 most recent posts, 5 most popular posts,
    and one post from each category.
    """
    recent_posts = Post.objects.filter(
        status="Approved").order_by('-created_on')[:4]
    favourite_posts = Post.objects.filter(
        status="Approved"
    ).annotate(
        like_count=Count('likes')).order_by('-like_count')[:4]
    
    context = {
        'recent_posts': recent_posts,
        'favourite_posts': favourite_posts
    }

    return render(request, 'home/index.html', context)