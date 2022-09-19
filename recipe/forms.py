"""
Creates the forms for crispy forms.
"""
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Comment, Recipe


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


class AddEditRecipeForm(forms.ModelForm):
    """
    Form to allow adding or editing the recipes on the site.
    """
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'categories', 'description',
                  'featured_image', 'instructions', 'time_taken',)


class MyChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyChangePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Submit'))
