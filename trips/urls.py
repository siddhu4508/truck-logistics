from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.trip_list, name='trip_list'),
    path('<int:trip_id>/', views.trip_detail, name='trip_detail'),
]
