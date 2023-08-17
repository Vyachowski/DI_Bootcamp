from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

