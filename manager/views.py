from django.shortcuts import render
from posts.models import Post, PostFlag


def manager_view(request):

    flags = PostFlag.objects.all()
    flagged_posts = Post.objects.filter(flag__in=flags)

    context = {
        'flagged_posts': flagged_posts,
    }
    return render(request, 'manager.html', context)
