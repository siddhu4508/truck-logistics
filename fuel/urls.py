from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.fuel_list, name='fuel_list'),
    path('<int:transaction_id>/', views.fuel_detail, name='fuel_detail'),
]
