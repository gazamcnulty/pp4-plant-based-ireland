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
from .forms import PostForm, GalleryForm, NewsForm, UserCreationForm  # CommentForm


# Create your views here.




def login_base(request):
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


@login_required(login_url='login_base')
def account(request):
    return render(request, 'account.html')


@login_required(login_url='login_base')
def change_password(request):
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
    posts = Post.objects.all()
    reports = News.objects.all()
    form = UserCreationForm()
    #paginator = Paginator(posts, 5)
    #page_number = request.GET.get("page")
    #page_obj = paginator.get_page(page_number)

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
        'posts': posts,
        'reports':reports,
        'form':form,
       # 'page_obj':page_obj,
    }
    return render(request, 'index.html', context)


def test_template(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'test_template.html', context)


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
            instance.user = request.user
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


def gallery(request):
    gallerys = Gallery.objects.all()
    context = {'gallerys':gallerys}
    return render(request, 'gallery.html', context)


@login_required(login_url='login_base')
def add_gallery(request):
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
    article= Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    breaking_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    context = {'reports':reports, 'blog_news':blog_news, 'recipe_news':recipe_news, 'posts':posts, 'categorys':categorys}
    return render(request, 'news.html', context)

def recipes(request):
    article= Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    new_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    context = {'reports':reports, 'posts':posts, 'blog_news':blog_news, 'recipe_news':recipe_news, 'categorys':categorys}
    return render(request, 'recipes.html', context)

def blogs(request):
    article= Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    new_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    context = {'reports':reports, 'posts':posts, 'blog_news':blog_news, 'recipe_news':recipe_news, 'categorys':categorys}
    return render(request, 'blogs.html', context)


def reviews(request):
    article= Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    new_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    context = {'reports':reports, 'posts':posts, 'blog_news':blog_news, 'recipe_news':recipe_news, 'review_news':review_news, 'categorys':categorys}
    return render(request, 'reviews.html', context)


def breaking_news(request):
    article= Article.objects.all()
    reports = News.objects.all()
    posts = Post.objects.all()
    blog_news = News.objects.filter(category__category='BLOG').filter(category__category='BLOG')
    recipe_news = News.objects.filter(category__category='RECIPE').filter(category__category='RECIPE')
    review_news = News.objects.filter(category__category='REVIEW').filter(category__category='REVIEW')
    breaking_news = News.objects.filter(category__category='NEWS').filter(category__category='NEWS')
    categorys = Article.objects.all()

    context = {'reports':reports, 'posts':posts, 'blog_news':blog_news, 'recipe_news':recipe_news, 'breaking_news':breaking_news, 'categorys':categorys}
    return render(request, 'breaking_news.html', context)

@login_required(login_url='login_base')
def add_news(request):
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
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'events.html', context)

