#Django imports, also function based views imported from views.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from pbi_app import views

#Url paths to dictate view logic linked with html template rendering
urlpatterns = [
    path('login_base/', views.login_base, name='login_base'),
    path('logout_base/', views.logout_base, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home_page, name='home_page'),
    path('about_us/', views.about_us, name='about_us'),
    path('search_results/', views.search_results, name='search_results'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit/<post_id>', views.edit_post, name='edit_post'),
    path('delete/<post_id>', views.delete_post, name='delete_post'),
    path('delete_comment/<comment_id>', views.delete_comment, name='delete_comment'),
    path('post_detail<int:post_id>', views.post_detail, name='post_detail'),
    path('post_like<int:post_id>', views.post_like, name='post_like'),
    path('gallery/', views.gallery, name='gallery'),
    path('add_gallery/', views.add_gallery, name='add_gallery'),
    path('news/', views.news, name='news'),
    path('add_news/', views.add_news, name='add_news'),
    path('recipes/', views.recipes, name='recipes'),
    path('blogs/', views.blogs, name='blogs'),
    path('reviews/', views.reviews, name='reviews'),
    path('breaking_news', views.breaking_news, name='breaking_news'),
    path('events/', views.events, name='events'),
    path('account/', views.account, name='account'),
    path('change_password/', views.change_password, name='change_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
