from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy

from posts.models import Post
from .models import UserProfile, User


# Create your views here.

def user_profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=user.pk)

    context = {
        'user': user,
        'posts': posts
    }

    return render(request, 'user_profile.html', context)

class UserSettingsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'profile_settings.html'
    fields = ['username', 'first_name', 'last_name', 'email']
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