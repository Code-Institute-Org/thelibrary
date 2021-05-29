from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse, reverse_lazy

from posts.models import Post
from .models import UserProfile, User


@login_required
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


class UserBookmarksView(LoginRequiredMixin, SingleObjectMixin, ListView):
    """
    Render page for user to view their bookmarks.
    """
    # Notes: Add ability to filter and sort bookmarks.
    paginate_by = 24
    template_name = 'bookmarks.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        return context

    def get_queryset(self):
        return self.object.post_bookmarks.all()


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
