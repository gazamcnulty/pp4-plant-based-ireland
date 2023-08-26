from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm  # CommentForm


# Create your views here.


def login_base(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User credentials not recognised. Please check and try again")


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, "User credentials not recognised. Please check and try again")
    context = {}
    return render(request, 'login_base.html', context)
#    messages.add_message(request, messages.INFO, "You have successfully logged out")


def logout_base(request):
    logout(request)
    return redirect('home_page')


def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def search_results(request):
    if request.method == "POST":
        search_response = request.POST['search_response']
        posts = Post.objects.filter(
            title__icontains=search_response)
        contents = Post.objects.filter(
            content__icontains=search_response)
        return render(request, 'search_results.html',
                      {'search_response': search_response, 'posts': posts, 'contents': contents})
    else:
        return render(request, 'search_results.html',
                      {'search_response': search_response})

    #    q = request.GET.get('q') if request.GET.get('q') != None else ''
    #    posts = Post.objects.filter(
    #        title__icontains=q, content__icontains=q)
    #    context = {
    #        'posts': posts
    #    }


def about_us(request):
    return render(request, 'about_us.html')

@login_required(login_url='login_base')
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
#            form.instance.user = request.user
            form.save()
            return redirect('home_page')
    context = {'form': form}
    return render(request, 'add_post.html', context)


@login_required(login_url='login_base')
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(instance=post)

    if request.user != post.author:
        return HttpResponse('You cannot edit posts submitted by other users')
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

@login_required(login_url='login_base')
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        return HttpResponse('You cannot delete posts submitted by other users')
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
