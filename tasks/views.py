from django.shortcuts import render, redirect
from .models import Task, Category
from .forms import TaskForm, CategoryForm, EditTaskForm

# Create your views here.
def home_view(request):
    return render(request, 'tasks/home.html')

def tasks_view(request, category):
    a = None if category == ' ' else category

    tasks = Task.objects.filter(category=a)
    categories = Category.objects.all()
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = TaskForm()

    context = {
        'tasks': tasks,
        'categories': categories,
        'form': form
    }

    return render(request, 'tasks/tasks.html', context)

def category_view(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()   
        return redirect('tasks_page')

    context = {
        'form': form
    }
    return render(request, 'tasks/category.html', context)

def edit_task_view(request, pk):
    task = Task.objects.get(pk=pk)

    a = task.category if task.category != None else ' '

    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_page', a)
    else:
        form = EditTaskForm(instance=task)

    context = {
        'task': task,
        'form': form
    }
    return render(request, 'tasks/edit_task.html', context)

def delete_task_view(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks_page', ' ')

    context = {
        'task': task
    }
    return render(request, 'tasks/delete_task.html', context)