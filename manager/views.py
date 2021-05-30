from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.models import Post, PostFlag


@login_required
def manager_view(request):
    """
    Render manager pg for library admins.
    Redirects non admins to the home page.
    """
    if not request.user.userprofile.is_admin:
        return redirect('home')
    else:
        flags = PostFlag.objects.all()
        flagged_posts = Post.objects.filter(flag__in=flags)

        context = {
            'flagged_posts': flagged_posts,
        }
        return render(request, 'manager.html', context)
