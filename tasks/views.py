from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
# Create your views here.

from projects.models import Project
from users.models import User
from datetime import date

def dashboard(request):

    # 🚫 if not logged in → go to login
    if not request.user.is_authenticated:
        return redirect('login')

    # 📊 get user tasks
    tasks = Task.objects.filter(assigned_to=request.user)

    # dropdown data
    projects = Project.objects.all()
    users = User.objects.all()

    # ➕ create task
    if request.method == "POST":
        Task.objects.create(
            title=request.POST['title'],
            project_id=request.POST['project'],
            assigned_to_id=request.POST['assigned'],
            due_date=request.POST['due']
        )
        return redirect('dashboard')

    # ⏰ overdue tasks
    overdue = tasks.filter(due_date__lt=date.today()).exclude(status='DONE')

    return render(request, "dashboard.html", {
        "tasks": tasks,
        "projects": projects,
        "users": users,
        "overdue": overdue.count()
    })
