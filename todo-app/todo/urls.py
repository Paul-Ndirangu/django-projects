# todo/urls.py

from django.urls import path
from todo import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "update/<int:task_id>/<str:new_status>",
        views.update_task_status,
        name = "update_status",
    ),
    path("delete/<int:task_id>", views.delete_task, name="delete"),
    path("filter/<str:status>", views.filter_tasks, name="filter"),
]
