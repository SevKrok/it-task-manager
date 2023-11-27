from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        related_name="workers",
        null=True
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return (
            f"{self.get_full_name()}, "
            f"username: {self.username}, position: {self.position}"
        )

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"pk": self.pk})


class TaskType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.TextChoices):
        URGENT = "U", "Urgent"
        HIGH = "H", "High"
        MEDIUM = "M", "Medium"
        LOW = "L", "Low"

    name = models.CharField(max_length=64)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    priority = models.CharField(
        max_length=6, choices=Priority.choices, default=Priority.MEDIUM
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.SET_NULL,
        null=True
    )
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self):
        return (
            f"Task: {self.name}, "
            f"status: {'Completed' if self.is_completed else 'In work'}, "
            f"priority: {self.priority}"
        )
