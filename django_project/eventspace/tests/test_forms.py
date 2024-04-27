from django.test import TestCase
from django.urls import reverse
from eventspace.forms import EventForm
from django.contrib.auth.models import User
import datetime

class EventFormTestCase(TestCase):
    def test_valid_form(self):
        data = {'title': 'Form Test Event', 'location': 'Testing town', 'date': datetime.datetime.today()}
        form = EventForm(data=data)
        self.assertTrue(form.is_valid())

    def test_missing_location_invalid(self):
        data = {'title': 'Form Test Event', 'date': datetime.datetime.today()}
        form = EventForm(data=data)
        self.assertFalse(form.is_valid() and self.assertIn('location', form.errors))

    def test_missing_title_invalid(self):
        data = {'title': '', 'date': datetime.datetime.today(), 'location': 'somewhere'}
        form = EventForm(data=data)
        self.assertFalse(form.is_valid() and self.assertIn('title', form.errors))

    def test_missing_date_invalid(self):
        data = {'title': 'Form Test Event', 'date': '', 'location': 'somewhere'}
        form = EventForm(data=data)
        self.assertFalse(form.is_valid() and self.assertIn('title', form.errors))