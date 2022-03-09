from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify       


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
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True, blank=True)
    favorite = models.ManyToManyField(User, related_name = "favorite_books")

    def __str__(self):
        return self.title

class Topic(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, blank=True, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Topic name={self.name}>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()