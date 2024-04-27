from django.test import TestCase
from django.contrib.auth.models import User
from eventspace.models import Event
import datetime

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password='password123')
        self.event = Event.objects.create(
            host = self.user,
            title = 'Unit test event',
            location = 'Testing town',
            description = 'Very cool unit tested event',
            date = '2024-04-24',
            start = '12:00:00',
        )
    def test_event_creation(self):
        self.assertEqual(self.event.host, self.user)
        self.assertEqual(self.event.title, 'Unit test event')
        self.assertEqual(self.event.location, 'Testing town')
        self.assertEqual(self.event.description, 'Very cool unit tested event')
        self.assertEqual(self.event.date, '2024-04-24')
        self.assertEqual(self.event.start, '12:00:00')