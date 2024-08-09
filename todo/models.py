from django.db import models

class Todo(models.Model):
    todo_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default="Not Started", choices=[
        ("Not Started", "Not Started"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ])        