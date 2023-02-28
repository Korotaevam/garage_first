from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Min
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .forms import AutoModelsPostForms
from .models import *
from .utils import *


# print(AutoModels.objects.filter(Q(pk=1) | Q(id__lt=4)))
# print(111, AutoModels.objects.order_by('pk').first())
# print(222, ModelAdd.objects.filter(automodels__group__contains='ЕЛЬ').distinct())
# print(222, ModelAdd.objects.aggregate(minimum=Min("pk")))
# print(444, AutoModels.objects.values('group').get(pk=1))


class IndexView(DataMixin):
    # model = AutoModels
    # template_name = 'garage_main/index.html'
    # context_object_name = 'model'
    # extra_context = {'title': 'Main Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_user_data(title='Main Page', **kwargs)
        # context['menu'] = menu
        # context['title'] = 'Main Page'
        # context['cat_select'] = 0
        return context

    def get_queryset(self):
        return AutoModels.objects.filter(is_published=True)

    # def index(request):


#     posts = AutoModels.objects.all()
#     context_menu = {'posts': posts,
#                     'model': menu,
#                     'title': 'Main Page',
#                     'cat_select': 0
#                     }
#     return render(request, 'garage_main/index.html', context=context_menu)


def about(request):
    posts = AutoModels.objects.all()
    return render(request, 'garage_main/about.html', {'title': 'About page', 'menu': menu, 'posts': posts})


def feedback(request):
    return HttpResponse(f'<h1> feedback <br> {request}</h1>')


class AddArticle(LoginRequiredMixin):
    pass


@login_required
def AddArticle(request):
    if request.method == 'POST':
        form = AutoModelsPostForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutoModelsPostForms()
    return render(request, 'garage_main/addpost.html', {'form': form, 'title': 'Add Article', 'menu': menu})


def login(request):
    return HttpResponse(f'<h1> Login <br> {request}</h1>')


def logout(request):
    return HttpResponse(f'<h1> logout <br> {request}</h1>')


def show_post(request, post_slug):
    posts = AutoModels.objects.filter(slug=post_slug)
    context_menu = {'posts': posts,
                    'menu': menu,
                    'title': 'Show post',
                    }
    return render(request, 'garage_main/show_post.html', context=context_menu)


def category(request, cat_id=0):
    if cat_id > 10:
        return redirect('home')
    return HttpResponse(f'<h1> Cat Page <br> {cat_id}</h1>')


# def show_models(request, model_add_id):
#     context_menu = {
#         'menu': menu,
#         'title': 'Show models',
#         'cat_select': model_add_id
#     }
#
#     return render(request, 'garage_main/index.html', context=context_menu)

class ShowModelsView(DataMixin):
    # model = AutoModels
    # template_name = 'garage_main/index.html'
    # context_object_name = 'model'

    # extra_context = {'title': 'Main Page'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_user_data(title='Show models', **kwargs)
        # context['menu'] = menu
        # context['title'] = 'Show models'
        # context['cat_select'] = self.kwargs['model_add_id_1']

        return context

    # def get_queryset(self):
    #     return AutoModels.objects.filter(is_published=True)

# cat_select=self.kwargs['model_add_id'],
