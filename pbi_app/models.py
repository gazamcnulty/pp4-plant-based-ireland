from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", null=True
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    featured_image = models.ImageField(
        upload_to='images/', default='placeholder_image', blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=80, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.body


class Gallery(models.Model):
    title = models.CharField(max_length=75, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='gallery_like', blank=True)
    featured_image = models.ImageField(
        upload_to='images/', default='placeholder_image', blank=True)

    class Meta:
        ordering = ["-created_on"]        

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Article(models.Model):
    category = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.category



class News(models.Model):
    title = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='link_like', blank=True)
    external_link = models.URLField()
    category = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()