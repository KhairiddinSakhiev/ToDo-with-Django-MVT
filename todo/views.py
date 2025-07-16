from django.shortcuts import render, HttpResponse, redirect

from .models import *

def task_list_view(request):
    if request.method == "GET":
        tasks = Task.objects.all().order_by("-id")
        return render(request, "task_list.html", {"tasks":tasks})


def task_create_view(request):
    if request.method == "GET":
        users = User.objects.all()
        return render(request, "task_create.html", {"users":users})
    elif request.method == "POST":
        title = request.POST.get("title", False)
        description = request.POST.get("description", False)
        due_date = request.POST.get("due_date", False)
        user_id = request.POST.get("user", False)
        if not title or not due_date or not user_id:
            return render(request, "task_create.html",
                           {"title":title, 
                            "description":description,
                            "due_date":due_date})
        user = User.objects.filter(id=user_id).first()
        Task.objects.create(
            title=title,
            description=description,
            user = user,
            due_date=due_date
        )
        return redirect("task_list")


def task_edit_view(request, pk):
    task = Task.objects.filter(id=pk).first()
    users = User.objects.all()
    if request.method == "GET":
        
        return render(request, "task_edit.html", {"task":task, "users":users})
    elif request.method == "POST":
        title = request.POST.get("title", False)
        description = request.POST.get("description", False)
        due_date = request.POST.get("due_date", False)
        user_id = request.POST.get("user", False)
        if not title or not due_date or not user_id:
            return render(request, "task_create.html",
                           {"title":title, 
                            "description":description,
                            "due_date":due_date,})
        user = User.objects.filter(id=user_id).first()
        
        task.title=title
        task.description=description
        task.user = user
        task.due_date=due_date
        task.save()
        return redirect("task_list")


def task_delete_view(request, pk):
    task = Task.objects.filter(id=pk).first()
    if not task:
        return HttpResponse("Task not found with id ", pk)
    if request.method == "GET":
        return render(request, "confirm_delete_task.html", {"task":task})
    elif request.method == "POST":
        task.delete()
        return redirect("task_list")
