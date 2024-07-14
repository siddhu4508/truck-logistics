# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.user_list, name='user_list')
]
