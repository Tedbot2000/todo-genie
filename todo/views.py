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
            # if the task name is over 20 chars long, truncate it in message and add ellipsis
            task_display = task[:20] + ("..." if len(task) > 20 else "")
            messages.success(request, f'Task "{task_display}" added successfully!')
        else:
            messages.error(request, 'Task cannot be empty.')
        return redirect('todo_list')
    todos = Todo.objects.all().order_by('id') # List items in the order of their IDs by default (override this when adding sorting filtering)
    return render(request, 'todo/todo_list.html', {'todos': todos})


def toggle_status(request, id):
    """
    Toggles the status of a task
    """
    todo = get_object_or_404(Todo, id=id)
    statuses = ["Not Started", "In Progress", "Completed"]
    current_index = statuses.index(todo.status)
    next_index = (current_index + 1) % len(statuses)
    todo.status = statuses[next_index]
    todo.save()
    # if the task name is over 20 chars long, truncate it in message and add ellipsis
    todo_display = todo.todo_name[:20] + ("..." if len(todo.todo_name) > 20 else "")
    messages.success(request, f'Status of "{todo_display}" updated to {todo.status}.')
    return redirect('todo_list')    


# def delete_todo(request, id):
#     """
#     Deletes a todo item by its ID.
#     """
#     todo = get_object_or_404(Todo, id=id)
#     todo.delete()
#     messages.success(request, 'Task deleted successfully.')
#     return redirect('todo_list')

def delete_task(request, id):
    """
    Deletes a todo item by its task name.
    """
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    # if the task name is over 20 chars long, truncate it in message and add ellipsis
    task_display = todo.todo_name[:20] + ("..." if len(todo.todo_name) > 20 else "")
    messages.success(request, f'Task "{task_display}" deleted successfully.')
    return redirect('todo_list')


def update_task(request, id):
    """
    Updates the status of a todo item to True.
    """
    todo = get_object_or_404(Todo, id=id)
    todo.status = True
    todo.save()
    # if the task name is over 20 chars long, truncate it in message and add ellipsis
    task_display = todo.todo_name[:20] + ("..." if len(todo.todo_name) > 20 else "")
    messages.success(request, f'Task "{task_display}" updated successfully.')
    return redirect('todo_list')
