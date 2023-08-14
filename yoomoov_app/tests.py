from django.test import TestCase
from django.urls import reverse


class ErrorhandlersTest(TestCase):

    # Test that a 403 error message redirects the user to the login page
    def test_handler403(self):
        response = self.client.get('accounts/login/?next=/dashboard')
        self.assertRedirects(response, reverse('account_login'))
