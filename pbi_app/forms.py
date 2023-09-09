from django import forms
from django.forms import EmailField 
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post , Gallery, News, Article # , Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user','title', 'content', 'featured_image']


class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# class CommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#        fields = ['name', 'body']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['user','title', 'featured_image']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['user', 'category', 'title', 'website', 'external_link']