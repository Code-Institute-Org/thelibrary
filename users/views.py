from django.shortcuts import render, get_object_or_404
from .models import UserProfile, User
from posts.models import Post

# Create your views here.

def user_profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=user.pk)

    context = {
        'user': user,
        'posts': posts
    }

    return render(request, 'user_profile.html', context)