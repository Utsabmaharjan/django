from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from user.forms import Createuser
from django.contrib.auth import authenticate

# Create your views here.

def user_list(request):
    user = User.objects.all()
    context = {
        "user": user
    }
    return render (request, 'user/index.html', context)

def create_user(request):
    form = Createuser()
    context = {
                "form": form
            }
    return render(request, 'user/create.html', context)

def login_user(request):
    form = AuthenticationForm()