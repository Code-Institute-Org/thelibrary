from django import forms
from django.forms.widgets import Widget
from users.models import UserProfile
from posts.models import PostCategory, PostTag
from slack.models import SlackChannel


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = PostCategory
        fields = ['name']


class CreateChannelForm(forms.ModelForm):
    class Meta:
        model = SlackChannel
        fields = ['name', 'slack_channel_id']


class CreatePostTag(forms.ModelForm):
    class Meta:
        model = PostTag
        fields = ['name']


class ManageUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['is_admin', 'is_mod', 'is_staff']
