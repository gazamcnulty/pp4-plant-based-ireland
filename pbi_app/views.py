#django imports for function based views

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Post, Comment, Gallery, News, Article
from .forms import PostForm, GalleryForm, NewsForm, UserCreationForm 


def login_base(request):
    """
    View for url path in urls, to render login_base.html template
    get username and password, authenticate user
    return render user back to home page

    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, "User credentials not recognised. Please check and try again")
    context = {}
    return render(request, 'login_base.html', context)


def register(request):
    """
    View for url path in urls, to render register.html template
    render UserCreationForm from forms.py, save user info, login user
    return render user back to home page
    """
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
    """
    No particular url linked to this view
    logout / de-authenticate user
    return render user back to home page
    """
    logout(request)
    return redirect('home_page')


@login_required(login_url='login_base')
def account(request):
    """
    View to allow for url path to render account.html
    show user info. decorator requires authentication first
    render account page
    @decorator requires login
    """
    return render(request, 'account.html')


@login_required(login_url='login_base')
def change_password(request):
    """
    View for url path to render account.html template
    show user info. decorator requires authentication first
    render account page
    @decorator requires login
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def home_page(request):
    """
    View for url path to render home page template
    passes objects from Post and News models into context, to be rendered in template
    passes in UserCreationForm for registration
    paginator variables for pagination with post objects
    render home page
    """
    posts = Post.objects.all()
    reports = News.objects.all()
    form = UserCreationForm()

    paginator = Paginator(posts, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

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
        #'posts': posts,
        'reports':reports,
        'form':form,
       'page_obj':page_obj,
    }
    return render(request, 'index.html', context)


def search_results(request):
    """
    View for url path to render account.html template
    show user info. decorator requires authentication first
    render account page
    """
    if request.method == "POST":
        search_response = request.POST['search_response']
        posts = Post.objects.filter(
            title__icontains=search_response)
        reports = News.objects.filter(
            title__icontains=search_response)
        return render(request, 'search_results.html',
                      {'search_response': search_response, 'posts': posts, 'reports': reports })
    else:
        return render(request, 'search_results.html',
                      {'search_response': search_response}
                      )


def about_us(request):
    """
    View for url path to render about_us.html template
    """
    return render(request, 'about_us.html')


@login_required(login_url='login_base')
def add_post(request):
    """
    View for url path to render add_post.html template
    use PostForm from forms.py to render and save form info
    render add_post.html page
    @decorator requires login
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home_page')
    
    form = PostForm()
    context = {'form': form}
    return render(request, 'add_post.html', context)


@login_required(login_url='login_base')
def edit_post(request, post_id):
    """
    View for url path to render edit_post.html template
    use PostForm from forms.py to edit post info
    return HttpResponse if user other than post creator
    render edit_post.html page
    @decorator requires login
    """
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



@login_required(login_url='login_base')
def delete_post(request, post_id):
    """
    View for url path to render delete.html template with user post passed in
    allow for post to be deleted
    return HttpResponse if user other than post creator
    render delete.html page
    @decorator requires login
    """
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.user:
        return HttpResponse('You cannot delete posts submitted by other users')
    if request.method == 'POST':
        post.delete()
        return redirect('home_page')
    context = {'obj': post}
    return render(request, 'delete.html', context)


def post_detail(request, post_id):
    """
    View for url path to render post_detail.html template
    view post content, likes, comments
    render post_detail.html page
    """
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all()
    number_of_likes = post.number_of_likes()
    reports = News.objects.all()

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('body')
        )
        return redirect('post_detail', post_id)
    context = {
        'post': post,
       'comments': comments,
        'number_of_likes': number_of_likes,
        'reports':reports,
    }
    return render(request, 'post_detail.html', context)



@login_required(login_url='login_base')
def delete_comment(request, comment_id):
    """
    View for url to render delete.html with comment passed in
    return Http reponse if not the user who created the comment
    allow user to delete their comment
    render delete.html page
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return HttpResponse('You cannot delete comments submitted by other users')
    if request.method == 'POST':
        comment.delete()
        return redirect('home_page')
    context = {'obj': comment}
    return render(request, 'delete.html', context)



def post_like(request, post_id):
    """
    View for url path to allow like / dislike of posts
    if else, either like or remove like when clicked
    render in post_detail.html page
    """
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', post_id)


def gallery(request):
    """
    View for url path to render gallery.html template
    passes objects from Gallery model, to be rendered in template
    render gallery html pge
    """
    gallerys = Gallery.objects.all()
    context = {'gallerys':gallerys}
    return render(request, 'gallery.html', context)


@login_required(login_url='login_base')
def add_gallery(request):
    """
    View for url path to render add_gallery.html template 
    uses GalleryForm from forms.py for user to add image
    save image and return user back to gallery
    @decorator requires login
    """
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('gallery')
    
    form = GalleryForm()
    context = {'form': form}
    return render(request, 'add_gallery.html', context)


def news(request):
    """
    View for url path to render news.html template 
    create variables for objects of Article, News, Post models
    create variables for category filters of News objects
    paginator variables for pagination with news objects
    render news.html page
    """
    article = Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()

    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    breaking_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    paginator = Paginator(reports, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        #'reports':reports,
        'blog_news':blog_news,
        'recipe_news':recipe_news,
        'posts':posts,
        'page_obj':page_obj,
        'categorys':categorys
        }
    return render(request, 'news.html', context)

def recipes(request):
    """
    View for url path to render recipes.html template 
    create variables for objects of Article, News, Post models
    create variables for category filters of News objects
    paginator variables for pagination with News/recipe objects
    render recipes.html page, with recipe objects filtered
    """
    article = Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    new_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    paginator = Paginator(recipe_news, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        #'reports':reports, 
        'posts':posts, 
        'page_obj':page_obj,
        'blog_news':blog_news, 
        'recipe_news':recipe_news, 
        'categorys':categorys
    }
    return render(request, 'recipes.html', context)

def blogs(request):
    """
    View for url path to render blogs.html template 
    create variables for objects of Article, News, Post models
    create variables for category filters of News objects
    paginator variables for pagination with News/blogs objects
    render blogs.html page, with blog objects filtered
    """
    article= Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    new_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    paginator = Paginator(blog_news, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            #'reports':reports,
            'posts':posts,
            'page_obj':page_obj,
            'blog_news':blog_news,
            'recipe_news':recipe_news,
            'categorys':categorys
            }
    return render(request, 'blogs.html', context)


def reviews(request):
    """
    View for url path to render reviews.html template 
    create variables for objects of Article, News, Post models
    create variables for category filters of News objects
    paginator variables for pagination with News/reviews objects
    render reviews.html page, with reviews objects filtered
    """
    article= Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    new_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    paginator = Paginator(review_news, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        #'reports':reports, 
        'posts':posts, 
        'page_obj':page_obj, 
        'blog_news':blog_news, 
        'recipe_news':recipe_news, 
        'review_news':review_news, 
        'categorys':categorys
        }
    return render(request, 'reviews.html', context)


def breaking_news(request):
    """
    View for url path to render breaking_news.html template 
    create variables for objects of Article, News, Post models
    create variables for category filters of News objects
    paginator variables for pagination with news/breaking_news objects
    render breaking_news.html page, with breaking_news objects filtered
    """
    article= Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    breaking_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    paginator = Paginator(breaking_news, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        #'reports':reports,
        'posts':posts,
        'page_obj':page_obj, 
        'blog_news':blog_news, 
        'recipe_news':recipe_news, 
        'breaking_news':breaking_news, 
        'categorys':categorys
        }
    return render(request, 'breaking_news.html', context)

@login_required(login_url='login_base')
def add_news(request):
    """
    View for url path to render add_news.html template 
    uses NewsForm from forms.py for user to add news article
    save post and return user back to news.html
    @decorator requires login
    """
    if request.method == 'POST':
        form = NewsForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('news')
    
    form = NewsForm()
    context = {'form': form}
    return render(request, 'add_news.html', context)


@login_required(login_url='login_base')
def events(request):
    """
    View for url path to render events.html template 
    return render events.html
    @decorator requires login
    """
    return render(request, 'events.html',)

