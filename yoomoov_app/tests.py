from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages


class ErrorHandlersTest(TestCase):

    # Test that a 403 error message redirects the user to the login page
    def test_handler403(self):
        response = self.client.get('/accounts/login/?next=/dashboard')
        self.assertRedirects(response, reverse('account_login'))

        messages = list(get_messages(response.wsgi_request))
        # tests that there is excatly 1 message
        self.assertEqual(len(messages), 1)
        # tests that the error message is 403 Error
        self.assertEqual(str(messages[0]), '403 Error: Access Denied')
