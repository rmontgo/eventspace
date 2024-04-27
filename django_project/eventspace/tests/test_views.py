from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from eventspace.models import Event
from django.utils import timezone

# Create your tests here.
class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password='password123')
        Event.objects.create(
            host = self.user,
            title = 'Unit test event',
            location = 'Testing town',
            description = 'Very cool unit tested event',
            date = '2024-04-26',
            start = '12:00:00'
        )
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventspace/index.html')
    
    def test_event_list_view(self):
        client = Client()
        response = client.get(reverse('event-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventspace/event_list.html')

    def test_login_view(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_user_page_redirect(self):
        client = Client()
        response = client.get(reverse('user_page'))
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'eventspace/user_page.html')