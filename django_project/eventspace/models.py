from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=False)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(("Date"), default=datetime.date.today, blank=False)
    start = models.TimeField(default=None, null=True, blank=True)
    end = models.TimeField(default=None, null=True, blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])