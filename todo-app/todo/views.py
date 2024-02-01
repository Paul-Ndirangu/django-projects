# todo/views.py
 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
 
from todo.forms import TaskForm
from todo.models import Task
 
 
def index(request: HttpRequest) -> HttpResponse:
    form = TaskForm()
    tasks = Task.objects.all().order_by("-created")
 
    context = {"tasks": tasks, "form": form}
 
    return render(request, "temp_index.html", context)
