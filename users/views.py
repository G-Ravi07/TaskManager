from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

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
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')