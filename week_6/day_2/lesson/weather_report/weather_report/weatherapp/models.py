from django.db import models

OPTIONS = [
    ('sn', 'sunny'),
    ('cl', 'cloudy'),
    ('wn', 'windy'),
    ('rn', 'rainy'),
    ('st', 'stormy'),
]


# Create your models here.
class Report(models.Model):
    location = models.CharField(max_length=50)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=OPTIONS)