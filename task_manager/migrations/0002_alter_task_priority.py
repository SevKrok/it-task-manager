# Generated by Django 4.2.7 on 2023-11-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("Urgent", "1"), ("High", "2"), ("Medium", "3"), ("Low", "4")],
                default="Medium",
                max_length=6,
            ),
        ),
    ]
