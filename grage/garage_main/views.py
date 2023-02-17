from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1> Main Page </h1>')

def category(request, cat_id=0):
    if cat_id>10:
        return redirect('home')
    return HttpResponse(f'<h1> Cat Page <br> {cat_id}</h1>')
