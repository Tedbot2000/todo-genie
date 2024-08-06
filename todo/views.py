from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Todo
from django.shortcuts import get_object_or_404, redirect


def todo_list(request):
    """
    Displays a list of all todo items and allows creation of new todo items.

    If the request method is POST, creates a new todo item with the provided task name.

    """
    if request.method == 'POST':
        task = request.POST.get('task')
        Todo.objects.create(todo_name=task)
        return redirect('todo_list')
    todos = Todo.objects.all().order_by('id') # List items in the order of their IDs by default
    return render(request, 'todo/todo_list.html', {'todos': todos})

def toggle_status(request, todo_name):
    """
    Toggles the status of a todo item.

    """
    # todo = get_object_or_404(Todo, todo_name=todo_name)
    # # Toggle status
    # if todo.status:
    #     todo.status = False
    # else:
    #     todo.status = True
    # todo.save()
    # return redirect('todo_list')

# def toggle_status(request, todo_name):
#     todo = Todo.objects.get(todo_name=todo_name)
#     if todo.status == "Not Started":
#         todo.status = "In Progress"
#     elif todo.status == "In Progress":
#         todo.status = "Completed"
#     else:
#         todo.status = "Not Started"
#     todo.save()
#     return redirect('todo_list')

#def toggle_status(request, todo_name):
    todo = Todo.objects.get(todo_name=todo_name)
    statuses = ["Not Started", "In Progress", "Completed"]
    current_index = statuses.index(todo.status)
    next_index = (current_index + 1) % len(statuses)
    todo.status = statuses[next_index]
    todo.save()
    return redirect('todo_list')


def delete_todo(request, id):
    """
    Deletes a todo item by its ID.

    """
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')


def delete_task(request, task_name):
    """
    Deletes a todo item by its task name.

    """
    Todo.objects.filter(todo_name=task_name).delete()
    return redirect('todo_list')


def update_task(request, task_name):
    """
    Updates the status of a todo item to True.

    """
    todo = Todo.objects.get(todo_name=task_name)
    todo.status = True
    todo.save()
    return redirect('todo_list')