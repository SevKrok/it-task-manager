from django.urls import path

from task_manager.views import (
    index,
    TaskListView,
    WorkerListView,
    WorkerDetailView,
    TaskDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
    assign_delete_worker_to_task,
    change_task_status,
    TaskTypeCreateView,
    PositionCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/worker-assign-delete/",
        assign_delete_worker_to_task,
        name="assign-delete-worker-to-task",
    ),
    path(
        "tasks/<int:pk>/change-task-status/",
        change_task_status,
        name="change-task-status",
    ),
    path(
        "tasks/task-type-create",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/position-create",
        PositionCreateView.as_view(),
        name="position-create"
    ),
]

app_name = "task_manager"
