# Generated by Django 4.2.11 on 2024-03-23 16:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_profile_pic'),
        ('cez', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='file',
        ),
        migrations.AddField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 30, 17, 58, 38, 81825)),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='content',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='temp')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cez.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
