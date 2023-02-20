
from django.urls import path
from garage_main.views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('post/<int:post_id>', show_post, name='show_post'),
    path('model_add/<int:model_add_id>', show_models, name='show_models'),

    path('cat/', category, name='category'),
    path('cat/<int:cat_id>', category, name='category_id'),
]


