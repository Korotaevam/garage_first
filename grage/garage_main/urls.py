
from django.urls import path
from garage_main.views import *


urlpatterns = [
    path('', index, name='home'),
    path('cat/', category, name='category'),
    path('cat/<int:cat_id>', category, name='category_id'),
]


