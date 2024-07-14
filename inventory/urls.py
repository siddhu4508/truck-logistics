from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.inventory_list, name='inventory_list'),
    path('<int:item_id>/', views.inventory_detail, name='inventory_detail'),
]
