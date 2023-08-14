from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import Client


class ErrorHandlersTest(TestCase):
    # Creates a user and logs the test user in to test the 404 redirect
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    # Test that a 404 error message redirects the user to the login page
    def test_handler404(self):
        response = self.client.get('/edit_booking/63')
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('account_login'), response['Location'])

