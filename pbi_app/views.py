from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


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
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'edit_post.html', context)
