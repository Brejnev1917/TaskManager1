import  os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TaskManagerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='normal_user', email='normal_user@example.com', password='password')
        self.guest = User.objects.create_user(username='guest', email='guest@example.com', password='password')
        self.url = reverse('your_view_url')
        self.view = TaskManagerViewTest.as_view()

    def test_normal_user_has_access(self):
        self.client.login(username='normal_user', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_guest_does_not_have_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/your-view-url/')