from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.tracking_list, name='tracking_list'),
    path('<int:tracking_id>/', views.tracking_detail, name='tracking_detail'),
]
