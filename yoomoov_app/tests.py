from django.test import TestCase, override_settings
from django.urls import reverse, path
from django.contrib.messages import get_messages
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


class CreateBookingTests(TestCase):

    # Creates a user and logs the test user in to test the CreateBooking
    # functions
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    # Tests for a succesfuly GET request when user is logged in
    def test_create_booking_get_request_user_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    # Tests for sucessful POST request when user is logged in
    def test_create_booking_post_request_user_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_booking'))
        data = {
            'first_name': 'Bob_test',
            'last_name': 'Brown',
            'email': 'bob@brown.com',
            'phone': '0123456789',
            'van_name': 'Large Van in Sheffield',
            'van_size': 'Large',
            'van_location': 'Sheffield',
            'van_county': 'South Yorkshire',
            'date_required': '01/12/2024',
            'price': '250'
        }
        response = self.client.post(reverse('create_booking'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')


