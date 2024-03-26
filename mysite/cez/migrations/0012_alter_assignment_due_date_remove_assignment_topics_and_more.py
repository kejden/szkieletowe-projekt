# Generated by Django 4.2.11 on 2024-03-25 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cez', '0011_alter_assignment_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 1, 9, 48, 22, 688671)),
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='topics',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='assignments',
        ),
        migrations.AddField(
            model_name='assignment',
            name='topics',
            field=models.ManyToManyField(blank=True, to='cez.topic'),
        ),
        migrations.AddField(
            model_name='topic',
            name='assignments',
            field=models.ManyToManyField(blank=True, to='cez.assignment'),
        ),
    ]