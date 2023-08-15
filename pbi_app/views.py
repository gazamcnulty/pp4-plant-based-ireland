from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about_us(request):
    return render(request, 'about_us.html')
