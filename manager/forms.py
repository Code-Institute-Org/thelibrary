from django import forms
from posts.models import PostCategory


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = PostCategory
        fields = ['name']
