from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Todo

def todo_list(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Todo.objects.create(todo_name=task)
        return redirect('todo_list')
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def delete_task(request, task_name):
    Todo.objects.filter(todo_name=task_name).delete()
    return redirect('todo_list')

def update_task(request, task_name):
    todo = Todo.objects.get(todo_name=task_name)
    todo.status = True
    todo.save()
    return redirect('todo_list')



# class HomePage(TemplateView): 
#     """ 
#     Displays home page" 
#     """ 
#     template_name = 'index.html'