from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.http import HttpResponse

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        # create user
        User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        return redirect('login')

    return render(request, "signup.html")


def login_view(request):
    return HttpResponse("LOGIN WORKING")

def logout_view(request):
    logout(request)
    return redirect('login')