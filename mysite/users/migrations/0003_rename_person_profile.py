# Generated by Django 4.2.11 on 2024-03-22 16:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_remove_person_lastname_remove_person_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Profile',
        ),
    ]