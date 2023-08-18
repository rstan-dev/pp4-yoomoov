from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponseServerError
from .models import Van, Booking, Feedback
from datetime import date, datetime
from decimal import Decimal


class DashboardiewTest(TestCase):
    # Test for successful retrieval of bookings and feedback for a
    # specific logged-in user

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
            )

        # Creates several Van Objects to test functions
        self.vans = [
            Van.objects.create(
                name='test Van 1',
                slug='test_van_1_live',
                size='Small',
                location='London',
                county='Greater London',
                crew=1,
                suitable_for='Suitable description',
                load_area_width=2.5,
                load_area_height=2.5,
                load_area_length=2.5,
                price='250.00',
                is_live=True
            ),

            Van.objects.create(
                name='test Van 2',
                slug='test_van_2_not_live',
                size='Medium',
                location='London',
                county='Greater London',
                crew=1,
                suitable_for='Suitable description',
                load_area_width=2.5,
                load_area_height=2.5,
                load_area_length=2.5,
                price='250.00',
                is_live=False
            ),
        ]

        self.live_van = self.vans[0]
        self.non_live_van = self.vans[1]

        # Create a test booking
        self.booking = Booking.objects.create(
            booking_number=1500,
            user_fk=self.user,
            van=self.live_van,
            first_name='TestCustomer',
            last_name='TestSurname',
            email='customer@email.com',
            phone='123456789',
            date_required='2030-01-01',
        )

        # Create several test feedback objects
        self.feedbacks = [
            Feedback.objects.create(
                booking=self.booking,
                booking_number=self.booking.booking_number,
                van=self.live_van,
                user_fk=self.user,
                title='test feedback title',
                comment='test feedback comments',
                rating=5,
                is_approved='Approved',
            ),
        ]

    def test_user_not_logged_in_redirects_to_login(self):
        # Test for a successful redirect to login screen if user
        # tries to access dashboard without logging in
        login_url = reverse('account_login')
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, f'{login_url}?next=/dashboard')

    def test_dashboard_template_renders_correctly(self):
        # Test to make sure the dashboard.html template
        # is called successfully, asserts a successful GET request
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_bookings_rendered_correctly_for_loggedin_user(self):
        # Tests that the bookings are displayed on dashboard for
        # a given user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard'))
        bookings = response.context['bookings']
        self.assertEqual(len(bookings), 1)

    def test_feeback_rendered_correctly_for_loggedin_user(self):
        # Tests that the feedbacks are displayed on dashboard for
        # a given user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard'))
        feedbacks = response.context['feedbacks']
        self.assertEqual(len(feedbacks), 1)


class CreateBookingTests(TestCase):
    # Tests the createBooking functionality
    def setUp(self):
        # Creates a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Creates a Van Object to test functions
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

        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    # Tests for a successful GET request when user is logged in
    def test_create_booking_get_request_user_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    # Tests for successful POST request when user is logged in and 302
    # response code
    def test_create_booking_post_request_user_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_booking'))
        data = {
            'first_name': 'Bob_test',
            'last_name': 'Brown',
            'email': 'bob@brown.com',
            'phone': '0123456789',
            'van': self.van.id,
            'date_required': '2025-12-01',
            'price': '250.00'
        }
        # Checks for a successful redirect code
        response = self.client.post(reverse('create_booking'), data)
        self.assertEqual(response.status_code, 302)

        # Checks if the data was created successfully
        created_booking = Booking.objects.last()
        self.assertEqual(created_booking.first_name, 'Bob_test')
        self.assertEqual(created_booking.last_name, 'Brown')
        self.assertEqual(created_booking.email, 'bob@brown.com')
        self.assertEqual(created_booking.phone, '0123456789')
        self.assertEqual(created_booking.van.name, 'Large Van in Sheffield')
        self.assertEqual(created_booking.date_required, date(2025, 12, 1))
        self.assertEqual(created_booking.price, Decimal('250.00'))


class EditBookingTests(TestCase):
    # Tests the editBooking functionality
    def setUp(self):
        # Creates a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Creates a Van Object to test functions
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
        # Creates a Booking object to test functions
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

    def test_edit_booking_successful_get_request(self):
        # Tests the GET request and checks booking form is prefilled correctly
        response = self.client.get(reverse('edit_booking',
                                           args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_booking_successfully_updated_data(self):
        # Tests the POST request with updated data returns successfully
        updated_data = {
            'first_name': 'Updated_Name',
            'last_name': 'Updated_Last_Name',
            'email': 'updated@email.com',
            'phone': '111222333444',
            'van': self.van.id,
            'date_required': '2025-01-01',
        }

        response = self.client.post(
                                    reverse('edit_booking',
                                            args=[self.booking.id]),
                                    updated_data
                                    )

        # Checks for a successful redirect code
        self.assertEqual(response.status_code, 302)

        # Checks if the data updated successfully]
        updated_booking = Booking.objects.get(id=self.booking.id)
        self.assertEqual(updated_booking.first_name, 'Updated_Name')
        self.assertEqual(updated_booking.last_name, 'Updated_Last_Name')
        self.assertEqual(updated_booking.email, 'updated@email.com')
        self.assertEqual(updated_booking.phone, '111222333444')
        self.assertEqual(updated_booking.van.name, 'Large Van in Sheffield')
        self.assertEqual(updated_booking.date_required, date(2025, 1, 1))


class DeleteBookingTests(TestCase):
    # Tests the deleteBooking functionality
    def setUp(self):
        # creates a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Creates a Van Object to test functions
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
        # Creates a Booking object to test functions
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

    def test_delete_booking_successful_get_request(self):
        # Tests the GET request and checks booking form is prefilled correctly
        response = self.client.get(reverse('delete_booking',
                                           args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_booking_successful_post_request(self):
        # Tests the POST request to the delete_booking view is successful
        response = self.client.post(reverse('delete_booking',
                                            args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

        # Confirms that the booking has been deleted from the database
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(id=self.booking.id)
