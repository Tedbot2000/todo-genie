from . import views
from django.urls import path
from .views import todo_list, delete_task, update_task

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('delete/<str:task_name>/', delete_task, name='delete'),
    path('update/<str:task_name>/', update_task, name='update'),
    path('toggle/<str:todo_name>/', views.toggle_status, name='toggle_status'),
]

# urlpatterns = [ 
#     path('', views.HomePage.as_view(), name='home'), 
# ]