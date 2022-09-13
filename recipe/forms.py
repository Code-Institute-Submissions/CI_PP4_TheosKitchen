"""
Creates the forms for crispy forms.
"""
from django.contrib.auth.models import User
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form users to post their comments.
    """
    class Meta:
        model = Comment
        fields = ('content', )


class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    class Meta:
        model = User
        fields = ('username', 'email')
