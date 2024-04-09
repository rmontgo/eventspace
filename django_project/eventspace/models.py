from django.db import models
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=False)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])