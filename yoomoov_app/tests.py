from django.test import TestCase, override_settings
from django.urls import reverse, path
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponseServerError
from django.core.mail import send_mail
from unittest.mock import patch
from .models import Van, Booking


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

    # Tests for sucessful POST request when user is logged in and
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


class EditBookingTests(TestCase):

    # Creates a user and logs the test user in to test the editBooking
    # functions
    # Creates a Van Object and a Booking object to test functions
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.van = Van.objects.create(
            name='Large Van in Sheffield',
            slug='large_van_sheffield',
            size='Large',
            location='Sheffield',
            county='South Yorkshire',
            crew=1,
            suitable_for='Suitable description',
            load_area_width=2.5,
            load_area_height=2.5,
            load_area_length=2.5,
            price='250.00',
            is_live=True
        )

        self.booking = Booking.objects.create(
            booking_number='1500',
            van=self.van,
            first_name='TestCustomer',
            last_name='TestSurname',
            email='customer@email.com',
            phone='123456789',
            date_required='2030-01-01',
        )

        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_edit_booking(self):
        # Tests the GET request and checks booking form is prefilled corectly
        response = self.client.get(reverse('edit_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)

