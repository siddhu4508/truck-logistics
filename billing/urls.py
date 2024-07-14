from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.billing_list, name='billing_list'),
    path('<int:billing_id>/', views.billing_detail, name='billing_detail'),
]
