from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pbi_app import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about_us/', views.about_us, name='about_us'),
    path('add', views.add_post, name='add_post'),
    path('edit/<post_id>', views.edit_post, name='edit_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
