from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy

from posts.models import Post
from .models import UserProfile, User


# Create your views here.

def user_profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    approved_posts = Post.objects.filter(author=user.pk, status='Approved')[:5]
    waiting_posts = Post.objects.filter(author=user.pk, status='Waiting')
    reviewed_posts = Post.objects.filter(author=user.pk, status='Review')

    context = {
        'user': user,
        'approved_posts': approved_posts,
        'waiting_posts': waiting_posts,
        'reviewed_posts': reviewed_posts,
    }

    return render(request, 'user_profile.html', context)

class UserSettingsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'user_settings.html'
    fields = ['username', 'first_name', 'last_name']
    success_message = "Update successful!"

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('settings', kwargs={'pk': pk})


def user_bookmarks_view(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    bookmarks = user_profile.bookmarks.all()
    total_bookmarks = bookmarks.count()

    context = {
        'bookmarks': bookmarks,
        'total_bookmarks': total_bookmarks
    }

    return render(request, 'bookmarks.html', context)

class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    fields = ['bio', 'profile_pic', 'linkedin', 'github']
    template_name = 'update_profile.html'
    success_message = "Your profile has been successfully updated!"

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('update_profile', kwargs={'pk': pk})


class PostsByAuthorView(ListView):
    paginate_by = 4
    template_name = 'posts_by_author.html'
    queryset = Post.objects.filter(status='Approved').order_by('-created_on')
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userprofile = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['author'] = userprofile.user.username
        return context