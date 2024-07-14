from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.dispatch_list, name='dispatch_list'),
    path('<int:dispatch_id>/', views.dispatch_detail, name='dispatch_detail'),
]
