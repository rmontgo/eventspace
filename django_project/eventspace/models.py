from django.db import models
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(blank=False)
    image = models.ImageField()
    description = models.TextField()