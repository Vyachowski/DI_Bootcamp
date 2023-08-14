from django.db import models


# Create your models here.
class Post(models.Model):
    # title
    title = models.CharField(max_length=50)
    # text
    text = models.TextField(blank=True, default='')
    # created_at
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
