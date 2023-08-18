from django.test import TestCase
from django.urls import reverse, path
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponseServerError


class ErrorHandlersTest(TestCase):
    # Test that a 404 error message redirects the user to the login page
    def test_handler404(self):
        response = self.client.get('/edit_booking/63')
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('account_login'), response['Location'])

    # Tests for a redirection if a user is not logged in
    def test_create_booking_when_not_logged_in(self):
        response = self.client.get(reverse('create_booking'))
        self.assertRedirects(response,
                             '/accounts/login/?next=%2Fcreate_booking%2F')
