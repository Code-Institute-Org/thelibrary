from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from posts.models import Post, PostFlag, PostCategory, PostTag
from users.models import UserProfile, User
from slack.models import SlackChannel
from .forms import (
    CreateCategoryForm,
    CreateChannelForm,
    CreatePostTag,
)


@login_required
def manage_flags(request):
    """
    Render manager pg for library admins.
    Redirects non admins to the home page.
    """
    if not request.user.userprofile.is_admin:
        return redirect('home')
    else:
        flags = PostFlag.objects.all()
        flagged_posts = Post.objects.filter(flag__in=flags)

        page = request.GET.get('page', 1)
        paginator = Paginator(flagged_posts, 24)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context = {
            'page_obj': page_obj,
        }
        return render(request, 'manage_flags.html', context)


@login_required
def profile_search(request):
    if not request.user.userprofile.is_admin:
        return redirect('home')
    else:
        q = request.GET.get('name_q')

        if q:
            if ' ' in q:
                names = q.split(' ', 1)
                first_name = names[0]
                last_name = names[1]
                users = User.objects.filter(
                    Q(userprofile__slack_display_name__icontains=q)
                    | Q(first_name__icontains=first_name)
                    | Q(last_name__icontains=last_name),
                )
            else:
                users = User.objects.filter(
                    Q(userprofile__slack_display_name__icontains=q)
                    | Q(first_name__icontains=q)
                    | Q(last_name__icontains=q),
                )

            page = request.GET.get('page', 1)
            paginator = Paginator(users, 24)
            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

        else:
            page_obj = 'none'

        context = {
            'page_obj': page_obj,
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
                    request, messages.SUCCESS,
                    "New category added successfully!")

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


@login_required
def manage_channels(request):
    if not request.user.userprofile.is_admin:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CreateChannelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "New channel added successfully!")

        channels = SlackChannel.objects.all().order_by('name')
        form = CreateChannelForm()
        context = {
            'channels': channels,
            'form': form
        }

        return render(request, 'manage_channels.html', context)


class EditChannel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SlackChannel
    template_name = 'edit_channel.html'
    fields = ['name', 'slack_channel_id']
    success_message = 'Slack channel successfully updated!'

    def get(self, request, *args, **kwargs):
        if not request.user.userprofile.is_admin:
            return redirect('home')
        else:
            return super(EditChannel, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('manage_channels')


@login_required
def manage_tags(request):
    if not request.user.userprofile.is_admin:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CreatePostTag(request.POST)
            if form.is_valid():
                form.save()

        form = CreatePostTag()

        context = {
            'tags': PostTag.objects.all().order_by('name'),
            'form': form,
        }

        return render(request, 'manage_tags.html', context)


class EditTag(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PostTag
    template_name = 'edit_tag.html'
    fields = ['name']
    success_message = 'Tag successfully updated!'

    def get(self, request, *args, **kwargs):
        if not request.user.userprofile.is_admin:
            return redirect('home')
        else:
            return super(EditTag, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('manage_tags')


def delete_tag(request, pk):
    if not request.user.userprofile.is_admin:
        return redirect('home')
    else:
        tag = get_object_or_404(PostTag, pk=pk)
        tag_name = tag.name
        tag.delete()
        messages.add_message(
            request, messages.SUCCESS, f"{tag_name} tag deleted!")

        return redirect('manage_tags')


class EditEditorsNote(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'edit_editors_note.html'
    fields = ['editors_note']
    success_message = 'Editors Note successfully updated!'

    def get(self, request, *args, **kwargs):
        if not request.user.userprofile.is_admin:
            return redirect('home')
        else:
            return super(EditEditorsNote, self).get(request, *args, **kwargs)

    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return reverse_lazy(
            'post_detail', kwargs={'pk': post.pk, 'slug': post.slug})


def delete_editors_note(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.editors_note = ''
    post.save()

    messages.add_message(
            request, messages.SUCCESS, "Editors note successfully deleted!")

    context = {
        'post': post
    }

    return render(request, 'post_detail.html', context)


class AddEditorsNote(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'add_editors_note.html'
    fields = ['editors_note']
    success_message = 'Editors Note successfully added!'

    def get(self, request, *args, **kwargs):
        if not request.user.userprofile.is_admin:
            return redirect('home')
        else:
            return super(AddEditorsNote, self).get(request, *args, **kwargs)

    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return reverse_lazy(
            'post_detail', kwargs={'pk': post.pk, 'slug': post.slug})


def delete_flag(request, pk):
    post_flag = get_object_or_404(PostFlag, pk=pk)
    post_flag.delete()
    messages.add_message(
            request, messages.SUCCESS, "Flag successfully dismissed")
    return redirect('manage_flags')
