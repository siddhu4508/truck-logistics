from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.driver_list, name='driver_list'),
    path('<int:driver_id>/', views.driver_detail, name='driver_detail'),
]
