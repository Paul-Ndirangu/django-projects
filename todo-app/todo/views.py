from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from todo.models import Task

# Views.

def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("-created")

    context = {"tasks": tasks}
    
    return render(request, "temp_index.html", context)
    