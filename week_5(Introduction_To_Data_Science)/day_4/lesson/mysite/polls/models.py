from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)