# Generated by Django 4.2.11 on 2024-03-25 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cez', '0010_alter_assignment_due_date_alter_enrollment_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='first_time_joined',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 1, 21, 44, 34, 965831)),
        ),
    ]
