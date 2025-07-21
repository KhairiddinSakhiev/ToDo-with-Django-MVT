from django.urls import path
from .views import *

urlpatterns = [
    path("", task_list_view, name='task_list'),
    path("create", task_create_view, name='task_create'),
    path("<int:pk>", task_edit_view, name='task_edit'),
    path("delete/<int:pk>", task_delete_view, name='task_delete'),
    path("complete/<int:pk>", complete_task_view, name='task_complete'),
]
