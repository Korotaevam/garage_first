from django.shortcuts import render, redirect
from django.http import HttpResponse

from garage_main.models import *

menu = ['About', 'Add article', 'Feedback', 'Login', 'Logout']


def index(request):
    posts = AutoModels.objects.all()
    return render(request, 'garage_main/index.html', {'title': 'Main page', 'menu': menu, 'posts': posts})


def about(request):
    posts = AutoModels.objects.all()
    return render(request, 'garage_main/about.html', {'title': 'About page', 'menu': menu, 'posts': posts})


def category(request, cat_id=0):
    if cat_id > 10:
        return redirect('home')
    return HttpResponse(f'<h1> Cat Page <br> {cat_id}</h1>')
