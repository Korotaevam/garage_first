
from django.urls import path
from garage_main.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('add_article/', AddArticle, name='add_article'),
    path('post/<slug:post_slug>', show_post, name='show_post'),

    path('model_add/<int:model_add_id_1>', ShowModelsView.as_view(), name='show_models'),


    path('cat/', category, name='category'),
    path('cat/<int:cat_id>', category, name='category_id'),
]


