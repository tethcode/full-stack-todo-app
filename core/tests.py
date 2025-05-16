from django.test import TestCase
from django.urls import reverse
from .models import TodoApp

# Test your Task model
class TaskModelTest(TestCase):
    def test_create_task(self):
        task = TodoApp.objects.create(title="Learn Django tests")
        self.assertEqual(task.title, "Learn Django tests")
        self.assertEqual(str(task), "Learn Django tests")  # assuming __str__ = title

# Test your homepage view
class HomePageViewTest(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse("home"))  # use the name from urls.py
        self.assertEqual(response.status_code, 200)
