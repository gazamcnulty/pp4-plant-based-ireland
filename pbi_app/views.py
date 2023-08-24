from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm  # CommentForm


# Create your views here.


def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
        title__icontains=q, content__icontains=q)
    context = {
        'posts': posts
    }
    return render(request, 'search.html')


def about_us(request):
    return render(request, 'about_us.html')


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    context = {'form': form}
    return render(request, 'add_post.html', context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    context = {
        'form': form
    }
    return render(request, 'edit_post.html', context)


# def delete_post(request, post_id):
#    post = get_object_or_404(Post, id=post_id)
#    post.delete()
#    return redirect('home_page')

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home_page')
    context = {'obj': post}
    return render(request, 'delete.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

#   ----------------------
#
#    new_comment = None
#
#    if request.method == 'POST':
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            new_comment = form.save(commit=False)
#            new_comment.post = post
#            new_comment.save()
#            return redirect('home_page')
#        else:
#            form = CommentForm()
#    form = CommentForm()
#
#
#   ---------------------
#    comments = post.comments.filter(approved=False)
#    comment_form = CommentForm(data=request.POST)
#    new_comment = None
#    if request.method == 'POST':
#        if comment_form.is_valid():
#            new_comment = comment_form.save(commit=False)
#            new_comment.post = post
#            new_comment.save()
#            return HttpResponseRedirect('/' + post.id)
#        else:
#            comment_form = CommentForm()
#   --------------
#    if request.method == 'POST':
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('post_detail')
#   ---------------
    context = {
        'post': post,
        #        'form': form
        #        'comments': comments,
        #        'new_comment': new_comment,
        #        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)
