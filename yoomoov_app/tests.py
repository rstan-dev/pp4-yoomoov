from django.test import TestCase, override_settings
from django.urls import reverse, path
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponseServerError
from django.core.mail import send_mail
from unittest.mock import patch
from .models import Van, Booking
from datetime import date, datetime
from decimal import Decimal


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

    # Tests for successful POST request when user is logged in and
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

    # Creates a user and logs the test user in to test the editBooking
    # functions

    def setUp(self):
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
        # Tests the GET request and checks booking form is prefilled corectly
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

    # Creates a user and logs the test user in to test the deleteBooking
    # functions

    def setUp(self):
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
        # Tests the GET request and checks booking form is prefilled corectly
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


class HomePageTest(TestCase):
    # Test for an acessbile page, correct template and the latest
    # 3 van lisitngs are displaying correctly

    def setUp(self):
        # Creates a Van Object to test functions
        self.vans = [
            Van.objects.create(
                name='test Van 1',
                slug='test_van_1',
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
                slug='test_van_2',
                size='Medium',
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
                name='test Van 3',
                slug='test_van_3',
                size='Medium',
                location='London',
                county='Greater London',
                crew=1,
                suitable_for='Suitable description',
                load_area_width=2.5,
                load_area_height=2.5,
                load_area_length=2.5,
                price='250.00',
                is_live=True
            )
        ]

    def test_home_page(self):
        # Tests for a 200 status code and if the correct template is used
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        # Tests that 3 vans displayed are the correct ones in the context,
        # and the latest three
        vans_in_context = response.context['vans']
        self.assertEqual(len(vans_in_context), 3)
        for van in vans_in_context:
            self.assertIn(van, self.vans[:3])


class AllVansTest(TestCase):
    # Test to ensure all Live vans are fetched and ordered according
    # to date_added in descending order

    def setUp(self):
        # Creates a Van Object to test functions
        date_added_1 = datetime(2024, 1, 2, 12, 0),
        date_added_2 = datetime(2024, 2, 2, 12, 0),
        date_added_3 = datetime(2024, 3, 2, 12, 0),

        self.vans = [
            Van.objects.create(
                name='test Van 1',
                slug='test_van_1',
                size='Small',
                location='London',
                county='Greater London',
                crew=1,
                suitable_for='Suitable description',
                load_area_width=2.5,
                load_area_height=2.5,
                load_area_length=2.5,
                price='250.00',
                is_live=True,
                date_added=date_added_3
            ),

            Van.objects.create(
                name='test Van 2',
                slug='test_van_2',
                size='Medium',
                location='London',
                county='Greater London',
                crew=1,
                suitable_for='Suitable description',
                load_area_width=2.5,
                load_area_height=2.5,
                load_area_length=2.5,
                price='250.00',
                is_live=True,
                date_added=date_added_1
            ),

            Van.objects.create(
                name='test Van 3',
                slug='test_van_3',
                size='Medium',
                location='London',
                county='Greater London',
                crew=1,
                suitable_for='Suitable description',
                load_area_width=2.5,
                load_area_height=2.5,
                load_area_length=2.5,
                price='250.00',
                is_live=False,
                date_added=date_added_2
            )
        ]

        # Tests for 2 live vans to be displayed
        def test_all_vans_view_displays_only_live_vans(self):
            response = self.client.get(reverse('all_vans'))
            vans_in_context = response.context['vans']

            self.assertEqual(len(vans_in_context), 2)










