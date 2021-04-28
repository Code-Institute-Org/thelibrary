from django.db.models import Q

from .models import PostCategory, Post


def categories(request):
    """ Generates categories for navbar on every page """
    return {'categories_nav': PostCategory.objects.all().order_by('name')}


def notifications(request):
    if request.user.is_authenticated:
        num_posts_in_review = Post.objects.filter(
            author=request.user.userprofile.id,
            status="Review"
        ).count()
        num_posts_to_review = Post.objects.filter(
            status="Waiting"
        ).exclude(author=request.user.userprofile).count()

        context = {
            'num_author_posts_in_review': num_posts_in_review,
            'num_posts_to_review': num_posts_to_review,
            'total_notifications': num_posts_in_review + num_posts_to_review,
        }

        return context
    else:
        return {}
