from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pbi_app import views


urlpatterns = [
    path('login_base/', views.login_base, name='login_base'),
    path('logout_base/', views.logout_base, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home_page, name='home_page'),
    path('about_us/', views.about_us, name='about_us'),
    path('search_results/', views.search_results, name='search_results'),
    path('add', views.add_post, name='add_post'),
    path('edit/<post_id>', views.edit_post, name='edit_post'),
    path('delete/<post_id>', views.delete_post, name='delete_post'),
    path('delete_comment/<comment_id>', views.delete_comment, name='delete_comment'),
    path('post_detail<int:post_id>', views.post_detail, name='post_detail'),
    #   path('test_comments/', views.test_comments, name='test_comments'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
