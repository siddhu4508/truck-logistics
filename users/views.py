# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import CustomUser

def index(request):
    return HttpResponse("Welcome to the Users app")


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'user':users})