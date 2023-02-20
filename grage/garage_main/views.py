from django.shortcuts import render, redirect
from django.http import HttpResponse

from garage_main.models import *

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Login', 'url_name': 'login'},
        {'title': 'Logout', 'url_name': 'logout'},
        ]


def index(request):
    posts = AutoModels.objects.all()
    model = ModelAdd.objects.all()
    context_menu = {'posts': posts,
                    'menu': menu,
                    'title': 'Main Page',
                    'model': model,
                    'cat_select': 0
                    }
    return render(request, 'garage_main/index.html', context=context_menu)


def about(request):
    posts = AutoModels.objects.all()
    return render(request, 'garage_main/about.html', {'title': 'About page', 'menu': menu, 'posts': posts})


def feedback(request):
    return HttpResponse(f'<h1> feedback <br> {request}</h1>')


def login(request):
    return HttpResponse(f'<h1> Login <br> {request}</h1>')


def logout(request):
    return HttpResponse(f'<h1> logout <br> {request}</h1>')


def show_post(request, post_id):
    return HttpResponse(f'<h1> show post <br> {post_id}</h1>')


def category(request, cat_id=0):
    if cat_id > 10:
        return redirect('home')
    return HttpResponse(f'<h1> Cat Page <br> {cat_id}</h1>')

def show_models(request, model_add_id):
    posts = AutoModels.objects.filter(model_add=model_add_id)
    model = ModelAdd.objects.all()

    context_menu = {'posts': posts,
                    'menu': menu,
                    'title': 'Main Page',
                    'model': model,
                    'cat_select': model_add_id
                    }

    return render(request, 'garage_main/index.html', context=context_menu)

