from . import views
from django.urls import path
from .views import todo_list, delete_task, update_task

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('toggle_status/<int:id>/', views.toggle_status, name='toggle_status'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('update/<int:id>/', views.update_task, name='update'),
    path('edit/<int:id>/', views.edit_task, name='edit'),
]
