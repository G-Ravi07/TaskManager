from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import User


# -------------------------
# SIGNUP
# -------------------------
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if username and password:
            User.objects.create_user(
                username=username,
                password=password,
                role=role
            )
            return redirect('login')

    return render(request, "signup.html")


# -------------------------
# LOGIN (SAFE VERSION)
# -------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return HttpResponse("Invalid credentials")

    return render(request, "login.html")


# -------------------------
# LOGOUT
# -------------------------
def logout_view(request):
    logout(request)
    return redirect('login')