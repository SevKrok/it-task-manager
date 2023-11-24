from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse
from django.utils import timezone

from task_manager.models import Position, Task, TaskType


WORKER_URL = reverse("task_manager:worker-list")
TASK_URL = reverse("task_manager:task-list")


class PublicTests(TestCase):
    def test_task_list_login_required(self):
        response = self.client.get(TASK_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_worker_list_login_required(self):
        response = self.client.get(WORKER_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateTaskTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tester",
            password="1best_tester1",
            position=Position.objects.create(name="QA")
        )
        self.client.force_login(self.user)

    def test_search_form_initial(self):
        response = self.client.get(TASK_URL)
        form = response.context["search_form"]

        self.assertEqual(form.initial["task_type"], "")

    def test_get_tasks(self):
        Task.objects.create(
            name="task1",
            description="description1",
            deadline=timezone.now() + timezone.timedelta(days=1),
            priority="High",
            is_completed=False,
            task_type=TaskType.objects.create(name="QA")
        )
        Task.objects.create(
            name="task2",
            description="description2",
            deadline=timezone.now() + timezone.timedelta(days=2),
            priority="Urgent",
            is_completed=False,
            task_type=TaskType.objects.create(name="Refactoring")
        )

        response = self.client.get(TASK_URL)
        tasks_list = list(Task.objects.all())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            tasks_list
        )
        self.assertTemplateUsed(
            response,
            "task_manager/task_list.html"
        )


class PrivateWorkerTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tester",
            password="1best_tester1",
            position=Position.objects.create(name="QA")
        )
        self.client.force_login(self.user)

    def test_get_workers(self):
        get_user_model().objects.create(
            username="username1",
            password="122334qwerty",
            first_name="first_name1",
            last_name="last_name1",
            email="user1@user.com",
            position=self.user.position
        )
        get_user_model().objects.create(
            username="username2",
            password="122334qwerty",
            first_name="first_name2",
            last_name="last_name2",
            email="user2@user.com",
            position=self.user.position
        )

        response = self.client.get(WORKER_URL)
        workers = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]),
            list(workers)
        )
        self.assertTemplateUsed(
            response,
            "task_manager/worker_list.html"
        )
