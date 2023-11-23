from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone

from task_manager.models import Worker, Task


def validate_deadline(deadline):
    datetime_now = timezone.now()
    if deadline < datetime_now:
        raise ValidationError("Deadline must be no earlier than today")

    return deadline


class TaskCreationForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        help_text="year-moth-day 00:00:00",
        widget=forms.DateTimeInput(
            attrs={
                'class': 'datetime-input'
            }
        ),
        input_formats=['%Y-%m-%d %H:%M:%S'],
        validators=[validate_deadline]
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskUpdateForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        help_text="year-moth-day 00:00:00",
        widget=forms.DateTimeInput(
            attrs={
                'class': 'datetime-input'
            }
        ),
        input_formats=['%Y-%m-%d %H:%M:%S'],
        validators=[validate_deadline]
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskSearchForm(forms.Form):
    task_type = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by task type"
            }
        )
    )


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
        )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            "first_name",
            "last_name",
            "email",
            "position",
        ]


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )
