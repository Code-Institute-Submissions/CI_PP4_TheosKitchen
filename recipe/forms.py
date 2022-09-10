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
