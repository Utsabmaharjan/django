from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.forms import RegisterForm
from django.contrib.auth import authenticate, login



# Create your views here.
def user_list(request):
    user = User.objects.all()
    context = {"user": user}
    return render(request, "user/index.html", context)


def create_user(request):
    form = RegisterForm()
    context = {"user": form}
    return render(request, "user/create.html", context)


def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        data = authenticate(username=username, password=password)
        if data is not None:
            login(request,data)
            return redirect("/")

    context = {"form": form}
    return render(request, "user/login.html", context)

def home(request):
    return render(request,'user/home.html')
