from django.db import models

class Todo(models.Model):
    todo_name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name