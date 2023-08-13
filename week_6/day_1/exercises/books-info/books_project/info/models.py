from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=100, blank=False)
    published_date = models.DateField(blank=False)
    description = models.TextField(blank=False)
    page_count = models.IntegerField(blank=False)
    categories = models.CharField(max_length=100, blank=False)
    thumbnail_url = models.URLField()
    objects = models.Manager()


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(validators=[MinLengthValidator(10)], blank=False)

