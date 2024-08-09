from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo

# Constant for statuses (more could be added later)
STATUSES = ["Not Started", "In Progress", "Completed"]

@login_required
def todo_list(request):
    """
    Displays a list of all todo items and allows creation of new todo items.
    """
    if request.method == 'POST':
        task = request.POST.get('task')
        if isinstance(task, str) and task.strip():  # is task a non-empty string?
            if len(task) > 60:
                messages.error(request, 'Task name cannot be more than 60 characters long.')
            else:
                # Todo.objects.create(todo_name=task)
                Todo.objects.create(todo_name=task, user=request.user)
                # if task name is over 20 chars long, truncate it in message and add ellipsis
                task_display = task[:20] + ("..." if len(task) > 20 else "")
                messages.success(request, f'Task "{task_display}" added successfully!')
        else:
            messages.error(request, 'Task cannot be empty.')
        return redirect('todo_list')
    # todos = Todo.objects.all().order_by('id')
    todos = Todo.objects.filter(user=request.user).order_by('id')
    return render(request, 'todo/todo_list.html', {'todos': todos})

def toggle_status(request, id):
    """
    Toggles the status of a task
    """
    todo = get_object_or_404(Todo, id=id, user=request.user)
    # todo = get_object_or_404(Todo, id=id)
    current_index = STATUSES.index(todo.status)
    next_index = (current_index + 1) % len(STATUSES)
    todo.status = STATUSES[next_index]
    todo.save()
    # if task name is over 20 chars long, truncate it in message and add ellipsis
    task_display = todo.todo_name[:20] + ("..." if len(todo.todo_name) > 20 else "")
    messages.success(request, f'Status of "{task_display}" updated to {todo.status}.')
    return redirect('todo_list')

def delete_task(request, id):
    """
    Deletes a todo item by its task name
    """
    todo = get_object_or_404(Todo, id=id, user=request.user)
    # todo = get_object_or_404(Todo, id=id)
    if todo:  # Check if the item exists before deleting
        todo.delete()
        # if task name is over 20 chars long, truncate it in message and add ellipsis
        task_display = todo.todo_name[:20] + ("..." if len(todo.todo_name) > 20 else "")
        messages.success(request, f'Task "{task_display}" deleted successfully.')
    return redirect('todo_list')

def update_task(request, id):
    """
    Updates the status of a todo item to True
    """
    todo = get_object_or_404(Todo, id=id)
    if todo:  # Check if the item exists before updating
        todo.status = True
        todo.save()
        # if task name is over 20 chars long, truncate it in message and add ellipsis
        task_display = todo.todo_name[:20] + ("..." if len(todo.todo_name) > 20 else "")
        messages.success