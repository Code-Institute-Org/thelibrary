from django import forms
from django.db.models import Count
from django.utils.translation import gettext_lazy as _
from .models import PostFlag, PostCategory, Post, PostTag


class FlagForm(forms.ModelForm):
    """
    Create form for users to flag posts.
    """
    INNAPPROPRIATE = 'Innappropriate content'
    OUTDATED = 'Outdated content'
    FLAG_REASONS = (
        (INNAPPROPRIATE, "Innappropriate content"),
        (OUTDATED, "Outdated content"),
    )
    reason = forms.ChoiceField(
        label="Please select the reason for flagging this post",
        choices=FLAG_REASONS,
        widget=forms.Select(attrs={'class': "form-select"}),
    )

    class Meta:
        model = PostFlag
        fields = ['reason']


class EditPostForm(forms.ModelForm):
    """
    Create form for edit post pg
    """
    category = forms.ModelChoiceField(
        queryset=PostCategory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    new_tags = forms.CharField(
        max_length=300, required=False,
        widget=forms.TextInput(
            attrs={
                'pattern': '[a-zA-Z0-9 ]+',
            }
        ))

    class Meta:
        model = Post
        fields = [
            'title',
            'summary',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'body',
            'category',
            'tags',
            'new_tags'
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }
