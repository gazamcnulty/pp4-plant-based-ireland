# Django imports to create forms, models import from models.py
from django import forms
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Gallery, News, Article


class PostForm(forms.ModelForm):
    """
    Dictate fields to be listed in post submission form
    Post form saves user input data to Post model
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']


class UserCreationForm(UserCreationForm):
    """
    Dictate fields to be listed in user registration form
    Lists email address as required
    UserCreationForm  saves user input data to User model
    """
    email = EmailField(label=_("Email address"), required=True,
                       help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class GalleryForm(forms.ModelForm):
    """
    Dictate fields to be listed in user gallery image submission form
    GalleryForm saves user input data to Gallery model
    """
    class Meta:
        model = Gallery
        fields = ['title', 'featured_image']


class NewsForm(forms.ModelForm):
    """
    Dictate fields to be listed in news article submission form
    NewsForm saves user input data to News model
    """
    class Meta:
        model = News
        fields = ['category', 'title', 'website', 'external_link']
