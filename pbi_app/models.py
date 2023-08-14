from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Content(models.Model):
    title_of_post = models.CharField(max_length=150, unique=True, null=False)
    photo = CloudinaryField('image', default='placeholder')
    extra_info = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    date_of_post = models.DateTimeField(auto_now_add=True)
    hearts = models.ManyToManyField(User, related_name='heart', blank=True)
    takeaway_available = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title_of_post
