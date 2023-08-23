from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm  # ,CommentForm


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


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('home_page')


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
