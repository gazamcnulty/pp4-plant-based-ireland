from django.contrib import admin
from django.urls import path, include
from pbi_app import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about_us/', views.about_us, name='about_us')
]
