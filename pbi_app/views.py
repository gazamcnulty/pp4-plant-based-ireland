from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
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


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, "Error occurred , registration not completed")
    context = {
        'form':form
    }
    return render (request, 'register.html', context)


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
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('home_page')
    
    form = PostForm()
    context = {'form': form}
    return render(request, 'add_post.html', context)


@login_required(login_url='login_base')
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(instance=post)

    if request.user != post.user:
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

    if request.user != post.user:
        return HttpResponse('You cannot delete posts submitted by other users')
    if request.method == 'POST':
        post.delete()
        return redirect('home_page')
    context = {'obj': post}
    return render(request, 'delete.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all()
    number_of_likes = post.number_of_likes()

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('body')
        )
        return redirect('post_detail', post_id)
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
       'comments': comments,
        'number_of_likes': number_of_likes,
        #'liked': liked,
        #        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)



@login_required(login_url='login_base')
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return HttpResponse('You cannot delete comments submitted by other users')
    if request.method == 'POST':
        comment.delete()
        return redirect('home_page')
    context = {'obj': comment}
    return render(request, 'delete.html', context)



def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', post_id)