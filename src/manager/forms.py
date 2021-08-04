from django import forms
from django.forms.widgets import Widget
from users.models import UserProfile
from posts.models import PostCategory, PostTag
from slack.models import SlackChannel


class CreateCategoryForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Category Name"
            }
        )
    )

    class Meta:
        model = PostCategory
        fields = ['name']


class CreateChannelForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "#channel-name"
            }
        )
    )
    slack_channel_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )

    class Meta:
        model = SlackChannel
        fields = ['name', 'slack_channel_id']


class CreatePostTag(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Tag"
            }
        )
    )

    class Meta:
        model = PostTag
        fields = ['name']


class ManageUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['is_admin', 'is_mod', 'is_staff']
