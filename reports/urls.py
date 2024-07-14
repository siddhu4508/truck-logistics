from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.report_list, name='report_list'),
    path('<int:report_id>/', views.report_detail, name='report_detail'),
]
