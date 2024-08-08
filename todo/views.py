from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo

@login_required
def todo_list(request):
    """
    Displays a list of all todo items and allows creation of new todo items.

    If the request method is POST, creates a new todo item with the provided task name.
    """
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            Todo.objects.create(todo_name=task)
            messages.success(request, 'Task added successfully!')
        else:
            messages.error(request, 'Task cannot be empty.')
        return redirect('todo_list')
    todos = Todo.objects.all().order_by('id') # List items in the order of their IDs by default
    return render(request, 'todo/todo_list.html', {'todos': todos})

def toggle_status(request, todo_name):
    """
    Toggles the status of a todo item.
    """
    todo = Todo.objects.get(todo_name=todo_name)
    statuses = ["Not Started", "In Progress", "Completed"]
    current_index = statuses.index(todo.status)
    next_index = (current_index + 1) % len(statuses)
    todo.status = statuses[next_index]
    todo.save()
    messages.success(request, f'Status of "{todo_name}" updated to {todo.status}.')
    return redirect('todo_list')

def delete_todo(request, id):
    """
    Deletes a todo item by its ID.
    """
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    messages.success(request, 'Task deleted successfully.')
    return redirect('todo_list')

def delete_task(request, task_name):
    """
    Deletes a todo item by its task name.
    """
    Todo.objects.filter(todo_name=task_name).delete()
    messages.success(request, f'Task "{task_name}" deleted successfully.')
    return redirect('todo_list')

def update_task(request, task_name):
    """
    Updates the status of a todo item to True.
    """
    todo = Todo.objects.get(todo_name=task_name)
    todo.status = True
    todo.save()
    messages.success(request, f'Task "{task_name}" updated successfully.')
    return redirect('todo_list')
