
from django.urls import path
from django.views.decorators.cache import cache_page

from garage_main.views import *


urlpatterns = [
    path('', cache_page(10)(IndexView.as_view()), name='home'),
    path('about/', about, name='about'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('register/', RegisterForm.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_article/', AddArticle, name='add_article'),
    path('post/<slug:post_slug>', show_post, name='show_post'),

    path('model_add/<int:model_add_id_1>', ShowModelsView.as_view(), name='show_models'),


    path('cat/', category, name='category'),
    path('cat/<int:cat_id>', category, name='category_id'),
]


