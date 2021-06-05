from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from posts.models import Post, Bookmark
from .models import UserProfile, User


def user_profile_view(request, pk):
    """
    Render selected users profile,
    including their 4 most recently published posts.
    """
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(
        author=user.pk, status='Published').order_by('-created_on')[:4]

    context = {
        'user': user,
        'posts': posts,
    }

    return render(request, 'user_profile.html', context)


@login_required
def dashboard_view(request):
    """
    Render dashboard view for logged in user. Displays all the posts
    the user has created in table format.
    """

    posts = Post.objects.filter(
        author=request.user.userprofile.pk).order_by('-created_on')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 24)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'dashboard.html', context)


@login_required
def bookmarks_view(request):
    """
    Render page for user to view their bookmarks.
    """
    bookmarks = Bookmark.objects.filter(user=request.user)
    sort_method = request.GET.get('sort_method', 'date')

    if sort_method == 'date' or sort_method == '':
        bookmarked_posts = Post.objects.filter(
            bookmarked_post__in=bookmarks
        ).order_by('-bookmarked_post__created_on')
    elif sort_method == 'category':
        bookmarked_posts = Post.objects.filter(
            bookmarked_post__in=bookmarks
        ).order_by('category__name')
    else:
        bookmarked_posts = Post.objects.filter(
            bookmarked_post__in=bookmarks
        ).order_by(sort_method)

    page = request.GET.get('page', 1)
    paginator = Paginator(bookmarked_posts, 24)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'bookmarks.html', context)


class UserSettingsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Render view for user to edit the settings
    associated with their User instance.
    """
    model = User
    template_name = 'user_settings.html'
    fields = ['username', 'first_name', 'last_name']
    success_message = "Update successful!"

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('settings', kwargs={'pk': pk})


class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Render view for user to edit the settings
    associated with their UserProfile instance.
    """
    model = UserProfile
    fields = ['bio', 'profile_pic', 'linkedin', 'github']
    template_name = 'update_profile.html'
    success_message = "Your profile has been successfully updated!"

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('update_profile', kwargs={'pk': pk})
