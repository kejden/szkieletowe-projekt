# Generated by Django 4.2.11 on 2024-04-22 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cez', '0041_merge_20240416_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 18, 9, 36, 228142)),
        ),
    ]
