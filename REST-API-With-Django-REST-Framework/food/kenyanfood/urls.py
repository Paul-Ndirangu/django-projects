# kenyanfood/urls.py
from django.urls import path
from . import views
from django.conf import settings 


urlpatterns = [
    path('', views.getFood),
    path('post/', views.postFood),
]
