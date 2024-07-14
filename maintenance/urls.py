from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.maintenance_list, name='maintenance_list'),
    path('<int:record_id>/', views.maintenance_detail, name='maintenance_detail'),
]
