from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from posts.models import Post, PostFlag, PostCategory
from users.models import UserProfile, User
from .forms import CreateCategoryForm


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


@login_required
def profile_search(request):
    if not request.user.userprofile.is_admin:
        return redirect('home')
    else:
        q = request.GET.get('name_q')
        if ' ' in q:
            names = q.split(' ', 1)
            first_name = names[0]
            last_name = names[1]
            users = User.objects.filter(
                Q(username__icontains=q)
                | Q(first_name__icontains=first_name)
                | Q(last_name__icontains=last_name),
            )
        else:
            users = User.objects.filter(
                Q(username__icontains=q)
                | Q(first_name__icontains=q)
                | Q(last_name__icontains=q),
            )
        context = {
            'users': users
        }
        return render(request, 'user_search.html', context)


class ManageUserProfile(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    fields = ['is_admin', 'is_mod', 'is_staff']
    template_name = 'manage_profile.html'
    success_message = 'This profile has been successfully updated!'

    def get(self, request, *args, **kwargs):
        if not request.user.userprofile.is_admin:
            return redirect('home')
        else:
            return super(ManageUserProfile, self).get(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('manage_user', kwargs={'pk': pk})


class ManageCategories(LoginRequiredMixin, ListView):
    template_name = 'manage_categories.html'
    model = PostCategory
    context_object_name = 'categories'

    def get(self, request, *args, **kwargs):
        if not request.user.userprofile.is_admin:
            return redirect('home')
        else:
            return super(ManageCategories, self).get(request, *args, **kwargs)


@login_required
def manage_categories(request):
    if not request.user.userprofile.is_admin:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CreateCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.INFO, "New category added successfully!")

        categories = PostCategory.objects.all().order_by('name')
        form = CreateCategoryForm()
        context = {
            'categories': categories,
            'form': form
        }

        return render(request, 'manage_categories.html', context)


class EditCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PostCategory
    template_name = 'edit_category.html'
    fields = ['name']
    success_message = 'Category name successfully updated!'

    def get(self, request, *args, **kwargs):
        if not request.user.userprofile.is_admin:
            return redirect('home')
        else:
            return super(EditCategory, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('manage_categories')
