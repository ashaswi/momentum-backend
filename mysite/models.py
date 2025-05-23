from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta

class PasswordResetCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_expired(self):
        return now() > self.created_at + timedelta(minutes=15)  # Expire after 15 minutes

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField()
    feeling = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.content

class Survey(models.Model):
    name = models.TextField()
    link = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self. name

class Task(models.Model):
    STATUSES = [
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    start_date = models.DateField()
    status = models.TextField()
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
