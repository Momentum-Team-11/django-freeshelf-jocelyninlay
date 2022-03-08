from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    description = models.TextField()
    url = models.CharField(max_length=750)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title