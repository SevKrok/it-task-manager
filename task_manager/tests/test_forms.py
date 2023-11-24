from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from task_manager.models import Position
from task_manager.forms import (TaskSearchForm,
                                WorkerSearchForm,
                                validate_deadline)


class FormsTest(TestCase):
    def setUp(self):
        self.worker_tester = get_user_model().objects.create(
            username="tester",
            password="1best_tester1",
            first_name="first_name1",
            last_name="last_name1",
            position=Position.objects.create(name="QA")
        )

    def test_tasks_search_form_by_task_type(self):
        form_data = {"name": "Refactoring"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_workers_search_form_by_username(self):
        form_data = {"username": "admin"}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_deadline_validation_with_invalid_data(self):
        with self.assertRaisesMessage(
                ValidationError,
                expected_message=(
                        "Oops! This deadline is not realistic. Try picking another time."
                )
        ):
            validate_deadline(timezone.now())
