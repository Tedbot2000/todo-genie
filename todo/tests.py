from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse

class TestTodoList(TestCase):
    def test_empty_task_submission(self):
        client = Client()
        response = client.post(reverse('todo_list'), {'task': ''})
        self.assertContains(response, 'Task cannot be empty.')