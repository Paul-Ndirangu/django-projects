from contextlib import AbstractContextManager
import datetime
from typing import Any

from django.db.models import QuerySet
from django.http import HttpResponse
from django.urls import reverse
from django.test import TestCase, Client

 
from todo.forms import TaskForm
from todo.models import Task

# App tests.

class TestTaskModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Creates a task instance that our tests can access.
        setUpTestData is executed once, so our task instance is
        shared between tests.
        """
        cls.task_name = "Learn Docker"
        cls.task = Task.objects.create(name=cls.task_name)
        
    def test_task_name(self):
        self.assertEqual(self.task.name, self.task_name)
        
    def test_task_default_status(self):
        """Test that our task was assigned a status of 'To Do'"""
        
        expected = Task.StatusChoice.TODO
        actual = self.task.status
        
        self.assertEqual(expected, actual)
        
    def test_task_created(self):
        """Tests that task.created stores a datetime"""
 
        self.assertEqual(type(self.task.created), datetime.datetime)
        
    def test_str(self):
        expected = f"To Do: {self.task_name}"
        actual = str(self.task)
        
        self.assertEqual(expected, actual)


class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("index")
        cls.client = Client()
        cls.task = Task.objects.create(name="Do a Python project")
        
    def test_index_view_returns_httpresponse(self):
        """Test our view returns a HttpResponse"""
        
        response = self.client.get(self.url)
        
        self.assertTrue(isinstance(response, HttpResponse))
        
    def test_status_code(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        
    def test_context(self):
        """Tests the context contains queryset of tasks"""
        response = self.client.get(self.url)
        
        self.assertIn("tasks", response.context)
        
        tasks = response.context["tasks"]
        
        self.assertTrue(isinstance(tasks, QuerySet))
        self.assertEqual(tasks.first(), self.task)
        
    def test_template_used(self):
        response = self.client.get(self.url)    
        self.assertTemplateUsed(response, "temp_index.html")
        
# todo/forms.py 
class TestTaskForm(TestCase):
    def test_form_instance(self):
        """Test that form has name field"""
        form = TaskForm()
 
        self.assertIn("name", form.fields)
 
    def test_is_valid(self):
        form = TaskForm(data={"name": "Book dentist appointment"})
 
        self.assertTrue(form.is_valid())
 
    def test_empty_form_invalid(self):
        form = TaskForm(data={"name": None})
 
        self.assertFalse(form.is_valid())


class TestUpdateView(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            name="Book dentist appointment", status=Task.StatusChoice.TODO
        )
        self.client = Client()
 
    def test_task_status_update(self):
        """Test the view updates the status of the task"""
        self.url = reverse("update_status", args=[self.task.id, Task.StatusChoice.DONE])
 
        self.assertEqual(self.task.status, Task.StatusChoice.TODO)
 
        response = self.client.get(self.url)
 
        self.assertEqual(response.status_code, 302)
 
        self.task.refresh_from_db()
 
        self.assertEqual(self.task.status, Task.StatusChoice.DONE)
 
    def test_task_status_update_raise_404(self):
        """Test a 404 is raised if attempts to update a task that doesn't exist"""
 
        bad_id = 999
        self.assertFalse(Task.objects.filter(id=bad_id).exists())
 
        url = reverse("update_status", args=[bad_id, Task.StatusChoice.DOING])
 
        response = self.client.get(url)
 
        self.assertEqual(response.status_code, 404)
 
    def test_task_status_update_bad_request(self):
        """Test a Bad Request is raised if user attempts to update status to a value
        that isn't one of the status choices"""
 
        invalid_status = "Not one of the choices"
 
        self.assertNotIn(invalid_status, Task.StatusChoice.values)
 
        url = reverse("update_status", args=[self.task.id, invalid_status])
 
        response = self.client.get(url)
 
        self.assertEqual(response.status_code, 400)
        

class TestDeleteTaskView(TestCase):
    def setUp(self):
        self.task = Task.objects.create(name="Book dentist appointment")
        self.client = Client()
 
    def test_delete_task(self):
        url = reverse("delete", args=[self.task.id])
 
        response = self.client.get(url)
 
        self.assertEqual(response.status_code, 302)
 
    def test_delete_task_deletes_task(self):
        url = reverse("delete", args=[self.task.id])
 
        self.assertEqual(Task.objects.count(), 1)
 
        self.client.get(url)
 
        self.assertEqual(Task.objects.count(), 0)
 
    def test_delete_task_raises_404(self):
        bad_id = 999
        self.assertFalse(Task.objects.filter(id=bad_id).exists())
 
        url = reverse("delete", args=[bad_id])
 
        response = self.client.get(url)
 
        self.assertEqual(response.status_code, 404)
        
             
        