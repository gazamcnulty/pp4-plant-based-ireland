from django.shortcuts import render
from django.http import HttpResponse
from .models import Content


# Create your views here.


def home_page(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about_us.html')
