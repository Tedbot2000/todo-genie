from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """
    Represents a task "Todo" item with a name and a status.
    """
    todo_name = models.CharField(
        max_length=60,
        help_text="The name of the Todo item (max 60 characters)"
    )
    status = models.CharField(
        max_length=20,
        default="Not Started",
        choices=[
            ("Not Started", "Not Started"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
        ],
        help_text="The status of the Todo item (choices: Not Started, In Progress, Completed)"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)