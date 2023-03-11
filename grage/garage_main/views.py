from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.cache import cache
from django.db.models import Q, Min
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .models import *
from .permissions import *
from .serializers import *
from .utils import *


# print(AutoModels.objects.filter(Q(pk=1) | Q(id__lt=4)))
# print(111, AutoModels.objects.order_by('pk').first())
# print(222, ModelAdd.objects.filter(automodels__group__contains='ЕЛЬ').distinct())
# print(222, ModelAdd.objects.aggregate(minimum=Min("pk")))
# print(444, AutoModels.objects.values('group').get(pk=1))


class IndexView(DataMixin):
    paginate_by = 2

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


class Feedback(DataMixin):
    # paginate_by = 3
    model = AutoModels
    template_name = 'garage_main/feedback.html'


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


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'garage_main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(title='Login', **kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


# def login(request):
#     return HttpResponse(f'<h1> Login <br> {request}</h1>')


def logout_user(request):
    logout(request)
    # print(111, reverse('login')) # <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/login/">
    return redirect('login')


class RegisterForm(CreateView):
    form_class = RegisterUserForm
    template_name = 'garage_main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(title='Register', **kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def show_post(request, post_slug):
    posts = cache.get('posts')
    if not cache:
        posts = AutoModels.objects.filter(slug=post_slug)
        cache.set('posts', posts, 10)

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

class ContactsFormView(FormView):
    form_class = ContactForm
    template_name = 'garage_main/contact.html'
    success_url = reverse_lazy('home')

    def get_user_data(self, *, object_list=None, title, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return redirect('home')


# class AutoModelsViewSet(viewsets.ModelViewSet):
#     queryset = AutoModels.objects.all()   # можно убрать
#     serializer_class = AutoSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if pk:
#             return AutoModels.objects.filter(pk=pk)
#
#         return AutoModels.objects.all()
#
#     @action(methods=['get'], detail=True)
#     def show_model(self, request, pk = None):
#         models_auto = ModelAdd.objects.get(pk=pk)
#         return Response({'models': models_auto.name})


class AutoModelsAPIList(generics.ListCreateAPIView):
    queryset = AutoModels.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AutoModelsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = AutoModels.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class AutoModelsAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = AutoModels.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsAdminOrReadOnly,)

# class AutoAPIView(APIView):
#     # queryset = AutoModels.objects.all()
#     # serializer_class = AutoSerializer
#
#     def get(self, request):
#         lst = AutoModels.objects.all()
#         return Response({'status': AutoSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = AutoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         # posts_new = AutoModels.objects.create(
#         #     articles=request.data['articles'],
#         #     group=request.data['group'],
#         #     subgroup=request.data['subgroup'],
#         #     group_add_id=request.data['group_add_id'],
#         #     sub_group_add_id=request.data['sub_group_add_id'],
#         #     model_add_id=request.data['model_add_id'],
#         #     photo=request.data['photo'],
#         #     slug=request.data['slug']
#         # )
#
#         # post_update_photo = model_to_dict(posts_new)
#         # post_update_photo["photo"] = str(post_update_photo["photo"])
#
#         return Response({'status': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'No pk'})
#
#         try:
#             instance = AutoModels.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object not found'})
#
#         serializer = AutoSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'status': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'No pk'})
#
#         try:
#             instance = AutoModels.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object not found'})
#
#         if not instance.is_published:
#             del_models = AutoModels.objects.filter(pk=pk)
#             del_models.delete()
#         else:
#             instance.is_published = False
#             instance.save()
#
#         return Response({'status': 'OK'})
