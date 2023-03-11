
from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework import routers

from garage_main.views import *

# router = routers.DefaultRouter()
# router.register(r'automodel', AutoModelsViewSet, basename='automodel')

urlpatterns = [
    path('', cache_page(10)(IndexView.as_view()), name='home'),
    path('about/', about, name='about'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('contact/', ContactsFormView.as_view(), name='contact'),
    path('register/', RegisterForm.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_article/', AddArticle, name='add_article'),
    path('post/<slug:post_slug>', show_post, name='show_post'),

    path('model_add/<int:model_add_id_1>', ShowModelsView.as_view(), name='show_models'),

    path('cat/', category, name='category'),
    path('cat/<int:cat_id>', category, name='category_id'),


    path('api/v1/automodel/', AutoModelsAPIList.as_view()),
    path('api/v1/automodel/<int:pk>/', AutoModelsAPIUpdate.as_view()),
    path('api/v1/automodel_delete/<int:pk>/', AutoModelsAPIDelete.as_view()),

    # path('api/v1/', include(router.urls)), # route

    # path('api/v1/automodel/', AutoModelsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('api/v1/automodel/<int:pk>/', AutoModelsViewSet.as_view({'put': 'update', 'delete': 'destroy'}))
    # path('api/v1/automodel/', AutoAPIList.as_view()),
    # path('api/v1/automodel/<int:pk>/', AutoAPIDetail.as_view()),
]


