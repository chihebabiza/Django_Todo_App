from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('home')

    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def clear_all_tasks(request):
    Task.objects.all().delete()
    return redirect('home')
