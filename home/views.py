from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from posts.models import Post, PostCategory


# Create your views here.
def home_view(request):
    """
    Render home page
    """
    recent_posts = Post.objects.filter(
        status="Approved").order_by('-created_on')[:5]
    favourite_posts = Post.objects.filter(
        status="Approved"
    ).annotate(like_count=Count('likes')).order_by('-like_count')[:5]
    
    categories = PostCategory.objects.all()
    items_by_category = []
    for cat in categories:
        items_by_category += Post.objects.filter(status="Approved", category=cat).order_by('?')[:1]
    
    context = {
        'recent_posts': recent_posts,
        'favourite_posts': favourite_posts,
        'items_by_category': items_by_category

    }
    return render(request, 'home/index.html', context)