from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date

from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer

from projects.models import Project
from users.models import User


# -------------------------
# DRF API VIEWSET
# -------------------------
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# -------------------------
# DASHBOARD VIEW (SAFE)
# -------------------------
def dashboard(request):
    return HttpResponse("DASHBOARD WORKING")