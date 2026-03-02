from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from apps.tasks.models import Task


User = get_user_model()


def get_access_token(user):
    """
    Helper function to generate JWT access token for a user
    """
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


class TaskAPITestCase(APITestCase):
    """
    Unit tests for Task CRUD APIs
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Generate JWT token
        token = get_access_token(self.user)

        # Attach token to client
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

        # Base URL
        self.tasks_url = "/api/tasks/"

    # ---------- AUTH TESTS ----------

    def test_unauthorized_user_cannot_access_tasks(self):
        """
        Ensure unauthenticated user cannot access tasks
        """
        self.client.credentials()  # remove token

        response = self.client.get(self.tasks_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    # ---------- CREATE ----------

    def test_create_task(self):
        """
        Authenticated user can create a task
        """
        data = {
            "title": "Test Task",
            "description": "Testing create task API"
        }

        response = self.client.post(
            self.tasks_url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(
            Task.objects.first().title,
            "Test Task"
        )

    # ---------- LIST ----------

    def test_list_tasks(self):
        """
        User can list only their tasks (paginated response)
        """
        Task.objects.create(title="Task 1", user=self.user)
        Task.objects.create(title="Task 2", user=self.user)

        response = self.client.get(self.tasks_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data["results"]), 2)

    # ---------- UPDATE ----------

    def test_update_task(self):
        """
        User can update their own task
        """
        task = Task.objects.create(
            title="Old Title",
            user=self.user
        )

        url = f"{self.tasks_url}{task.id}/"

        response = self.client.patch(
            url,
            {"title": "Updated Title"},
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        task.refresh_from_db()
        self.assertEqual(task.title, "Updated Title")

    # ---------- DELETE ----------

    def test_delete_task(self):
        """
        User can delete their own task
        """
        task = Task.objects.create(
            title="Delete Me",
            user=self.user
        )

        url = f"{self.tasks_url}{task.id}/"

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(Task.objects.count(), 0)