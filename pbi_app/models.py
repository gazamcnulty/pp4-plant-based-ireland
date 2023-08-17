from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", null=True
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# class Comment(models.Model):
#    post = models.ForeignKey(Post, on_delete=models.CASCADE,
#                             related_name="comments")
#    name = models.CharField(max_length=80)
#    body = models.TextField()
#    created_on = models.DateTimeField(auto_now_add=True)
#    approved = models.BooleanField(default=False)
#
#    class Meta:
#        ordering = ["created_on"]
#
#    def __str__(self):
#        return f"Comment {self.body} by {self.name}"
