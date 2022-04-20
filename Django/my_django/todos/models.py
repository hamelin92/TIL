from django.db import models
from django.forms import BooleanField, DateTimeField
from django.conf import settings

# Create your models here.


class Todo(models.Model):
    title = models.TextField()
    completed = models.BooleanField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title