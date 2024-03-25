from django.db import models
from users.models import Profile
from datetime import datetime, timedelta
import shutil
import os

class Assignment(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    due_date = models.DateTimeField(default=datetime.now() + timedelta(weeks=1))
    topics = models.ManyToManyField('Topic', blank=True)

    def __str__(self):
        return f"{self.title}"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='temp')

    # '''W dalszej części jeżeli będzie potrzeba to plik będzie zapisywany do folderu danego zadania'''
    # def save(self, *args, **kwargs ):
    #     super().save(*args, **kwargs)
    #     directory = f"/assignments/{self.pk}/"
    #     os.makedirs(directory, exist_ok=True)
    #     print(f"{self.file}") 
    #     shutil.move(f"/{self.file}", directory)
    #     self.file = new_file
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Answer submitted by {self.student} to {self.assignment}"

class Topic(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    files = models.ManyToManyField('File',blank=True)
    assignments = models.ManyToManyField('Assignment',blank=True)

    def __str__(self):
        return f"{self.title}"

class File(models.Model):
    file = models.FileField(upload_to='pdf_files/')

    def __str__(self):
        return f"{self.file.name}"