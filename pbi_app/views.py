from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post


# Create your views here.


def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def about_us(request):
    return render(request, 'about_us.html')


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('form_title')
        content = request.POST.get('form_content')
        Post.objects.create(title=title, content=content)
        return redirect('')

    return render(request, 'add_post.html')
