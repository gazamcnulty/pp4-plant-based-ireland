from django import forms
from .models import Post , Gallery, News, Article # , Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user','title', 'content', 'featured_image']


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