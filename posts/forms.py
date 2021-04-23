from django import forms
from .models import PostFlag

class FlagForm(forms.ModelForm):
    class Meta:
        model = PostFlag
        fields = ['reason']