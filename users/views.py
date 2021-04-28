from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse, reverse_lazy

from posts.models import Post
from .models import UserProfile, User


# Create your views here.

@login_required
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


class UserBookmarksView(LoginRequiredMixin, SingleObjectMixin, ListView):
    paginate_by = 4
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


class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    fields = ['bio', 'profile_pic', 'linkedin', 'github']
    template_name = 'update_profile.html'
    success_message = "Your profile has been successfully updated!"

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('update_profile', kwargs={'pk': pk})
