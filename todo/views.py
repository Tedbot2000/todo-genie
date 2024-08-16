from django.db.models import Case, When, IntegerField
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo


# Constant for statuses (enabling more to be added later)
STATUSES = ["Not Started", "In Progress", "Completed"]


@login_required
def todo_list(request):
    """
    Displays a list of all tasks and allows creation of new tasks items.
    """
    if request.method == 'POST':
        task = request.POST.get('task')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        # is task a non-empty string?
        if isinstance(task, str) and task.strip():
            if len(task) > 60:
                messages.error(request,
                               'Task name cannot be more '
                               'than 60 characters long.')
            else:
                Todo.objects.create(todo_name=task, user=request.user, due_date=due_date,
                    priority=priority)
                # if task name is over 20 chars long, truncate & add ellipsis
                task_display = task[:20] + ("..." if len(task) > 20 else "")
                messages.success(request, f'Task "{task_display}'
                                 '" added successfully!')
        else:
            messages.error(request, 'Task cannot be empty.')
        return redirect('todo_list')
    
    sort_by = request.GET.get('sort_by', 'priority')  # Default to sorting by due date
    if sort_by not in ['priority', 'due_date']:
        sort_by = 'priority'

    # Order the tasks based on the selected sorting option
    if sort_by == 'priority':
        todos = Todo.objects.filter(user=request.user).order_by(
            Case(
                When(priority='High', then=1),
                When(priority='Medium', then=2),
                When(priority='Low', then=3),
                default=4,  # In case priority is None or invalid
                output_field=IntegerField(),
            ),
            'due_date'  # Secondary sorting by due date to ensure consistent ordering
        )
    elif sort_by == 'due_date':
        todos = Todo.objects.filter(user=request.user).order_by('due_date', 'priority')
    return render(request, 'todo/todo_list.html', {'todos': todos, 'sort_by': sort_by})


def toggle_status(request, id):
    """
    Toggles the status of a task
    """
    todo = get_object_or_404(Todo, id=id, user=request.user)
    current_index = STATUSES.index(todo.status)
    next_index = (current_index + 1) % len(STATUSES)
    todo.status = STATUSES[next_index]
    todo.save()
    # truncate task name to 20 chars
    task_display = todo.todo_name[:20] + (
        "..." if len(todo.todo_name) > 20 else "")
    messages.success(
        request, f'Status of "{task_display}" updated to {todo.status}.')
    return redirect('todo_list')


def delete_task(request, id):
    """
    Deletes a tasl by its task name
    """
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if todo:  # Check if the item exists before deleting
        todo.delete()
        # truncate task name to 20 chars
        task_display = todo.todo_name[:20] + (
            "..." if len(todo.todo_name) > 20 else "")
        messages.success(
            request, f'Task "{task_display}" deleted successfully.')
    return redirect('todo_list')


def update_task(request, id):
    """
    Updates the status of a task to True
    """
    todo = get_object_or_404(Todo, id=id)
    if todo:  # Check if the item exists before updating
        todo.status = True
        todo.save()
        # truncate task name to 20 chars
        task_display = todo.todo_name[:20] + (
            "..." if len(todo.todo_name) > 20 else "")
        messages.success


def edit_task(request, id):

    """

    Edits a task

    """

    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == 'POST':

        task_name = request.POST.get('task')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        if task_name:

            if len(task_name) > 60:

                messages.error(request, 'Task name '
                               'cannot be more than 60 characters long.')

            else:

                todo.todo_name = task_name
                todo.due_date = due_date
                todo.priority = priority
                todo.status = status

                todo.save()

                messages.success(
                    request, f'Task "{task_name}" updated successfully.')

                return redirect('todo_list')

    return render(request, 'todo/edit_task.html', {'todo': todo})
