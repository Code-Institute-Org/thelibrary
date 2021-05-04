from django import forms
from django.utils.translation import gettext_lazy as _
from .models import PostFlag


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
