# Generated by Django 4.2.11 on 2024-03-24 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cez', '0006_file_alter_assignment_due_date_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 17, 10, 16, 636446)),
        ),
    ]
