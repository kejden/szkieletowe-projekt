# Generated by Django 4.2.11 on 2024-04-01 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cez', '0028_alter_assignment_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 18, 25, 5, 960703)),
        ),
    ]
