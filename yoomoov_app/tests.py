from django.test import TestCase, override_settings
from django.urls import reverse, path
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponseServerError
from django.core.mail import send_mail
from unittest.mock import patch
from .models import Van, Booking, Feedback
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
        # Creates several Van Objects to test functions
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
        # Creates several Van Objects to test functions
        date_added_1 = datetime(2024, 1, 2, 12, 0)
        date_added_2 = datetime(2024, 2, 2, 12, 0)
        date_added_3 = datetime(2024, 3, 2, 12, 0)

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

    # Tests for 2 live vans to be displayed in descending date order
    def test_all_vans_view_displays_only_live_vans(self):
        response = self.client.get(reverse('all_vans'))
        vans_in_context = response.context['vans']

        self.assertEqual(len(vans_in_context), 2)
        self.assertEqual(vans_in_context[0].name, 'test Van 1')
        self.assertEqual(vans_in_context[1].name, 'test Van 2')


class ServicesTest(TestCase):
    # Test to ensure Services Page is using the correct template
    def test_services_template(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services.html')


class ContactFormTest(TestCase):
    # Tests the contact form submits a POST request correctly
    # and displays a success message after form is submitted.  Also checks
    # for if there is a slug, and if so the redirect should be back to the
    # van page or redirect to the home page.

    def setUp(self):
        # Creates a Van Object to test contact form with slug
        date_added_3 = datetime(2024, 1, 2, 12, 0)

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
            )
        ]

        # Creates a test form with data
        self.form_data = {
            'name': 'Test name',
            'email': 'test@email.com',
            'message': 'test message left'
        }

    # Test to ensure the correct template is used
    def test_contact_form_template_successful(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    # Test to ensure the POST request is successful and a sucess
    # message is displayed after redirect
    def test_contact_form_post_successful(self):
        response = self.client.post(reverse('contact'),
                                    self.form_data, follow=True)

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your message has been sent! "
                                           "We will respond within 24 hours.")

    # Test to check contact form redirects back to correct van_detail page
    # using the slug
    def test_contact_form_slug_redirects_back_to_van_detail_page(self):
        response = self.client.post(reverse('contact_from_van',
                                            kwargs={'slug': 'test_van_1'}),
                                    self.form_data)
        self.assertRedirects(response, reverse('van_detail',
                                               kwargs={'slug': 'test_van_1'}))

    # Test to check contact form redirects back to hone page if no slug
    # is present
    def test_contact_form_no_slug_redirects_to_home(self):
        response = self.client.post(reverse('contact'), self.form_data)
        self.assertRedirects(response, reverse('home'))


class VanDetailViewTest(TestCase):
    # Test for successful retirval of van detail page based on a valid slug.
    # Test for a 404 redirect if there is an invalid slug
    # Test for only live van listings displayed

    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username='testuser')

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

            Feedback.objects.create(
                booking=self.booking,
                van=self.live_van,
                user_fk=self.user,
                title='test feedback title2',
                comment='test feedback comments2',
                rating=5,
                is_approved='Pending',
            )
        ]

        self.approved_feedback = self.feedbacks[0]
        self.pending_feedback = self.feedbacks[1]

    # Test if live van is successfully retrieved and serves a 200 success code
    def test_live_van_detail_successful_retrieval(self):
        live_van = Van.objects.get(slug='test_van_1_live')
        response = self.client.get(reverse('van_detail',
                                           kwargs={'slug': live_van.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'van_detail.html')

    # Test if non-live van is successfully redirected serving a 302 code
    def test_non_live_van_detail_successful_redirect(self):
        non_live_van = Van.objects.get(slug='test_van_2_not_live')
        response = self.client.get(reverse('van_detail',
                                           kwargs={'slug': non_live_van.slug}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login'))

    # Test if van_detail displays only_approved_feedback
    def test_van_detail_displays_only_approved_feedback(self):
        live_van = Van.objects.get(slug='test_van_1_live')
        response = self.client.get(reverse('van_detail',
                                           kwargs={'slug': live_van.slug}))
        self.assertEqual(len(response.context['van_feedbacks']), 1)
        for feedback in response.context['van_feedbacks']:
            self.assertEqual(feedback.is_approved, 'Approved')


class VanSearchResultsTest(TestCase):
    # Tests if van search results displays vans according to selected filters,

    def setUp(self):
        # Creates several Van Objects to test functions
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
            ),

            Van.objects.create(
                name='test Van 4',
                slug='test_van_4',
                size='Large',
                location='Stockport',
                county='Greater Manchester',
                crew=2,
                suitable_for='Suitable description',
                load_area_width=2.5,
                load_area_height=2.5,
                load_area_length=2.5,
                price='250.00',
                is_live=True
            )
        ]

        self.test_van_1 = self.vans[0]
        self.test_van_2 = self.vans[1]
        self.test_van_3 = self.vans[2]
        self.test_van_4 = self.vans[3]

    def test_van_search_displays_correct_template(self):
        # Tests for a 200 status code and if the correct template is used
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'van_filter.html')

    def test_van_search_displays_no_filter(self):
        # Tests if all vans are displayed if no filter is used and Search
        # button is clicked
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['vans']), len(self.vans))

    def test_van_search_with_size_filter(self):
        # Tests if the correct vans are displayed when the size filter is
        # applied.
        # Checks for any vans that = Medium, then checks if the
        # number of medium vans in the response = the number of medium vans
        # in the database.
        size_filter = 'Medium'
        response = self.client.get(reverse('search'), {'van-size':
                                                       size_filter})
        self.assertEqual(response.status_code, 200)

        medium_vans = [van for van in self.vans if van.size == size_filter]

        self.assertEqual(len(response.context['vans']), len(medium_vans))

        for van in medium_vans:
            self.assertIn(van, response.context['vans'])

    def test_van_search_with_location_filter(self):
        # Tests if the correct vans are displayed when the location filter is
        # applied.
        # Checks for any vans that = London, then checks if the
        # number of London vans in the response = the number of London vans
        # in the database.
        location_filter = 'London'
        response = self.client.get(reverse('search'), {'location':
                                                       location_filter})
        self.assertEqual(response.status_code, 200)

        london_vans = [van for van in self.vans if van.location ==
                       location_filter]

        self.assertEqual(len(response.context['vans']), len(london_vans))

        for van in london_vans:
            self.assertIn(van, response.context['vans'])

    def test_van_search_with_county_filter(self):
        # Tests if the correct vans are displayed when the county filter is
        # applied.
        # Checks for any vans that = Greater London, then checks if the
        # number of Greater London vans in the response = the number of
        # Greater London vans in the database.
        county_filter = 'Greater London'
        response = self.client.get(reverse('search'), {'county':
                                                       county_filter})
        self.assertEqual(response.status_code, 200)

        greater_london_vans = [van for van in self.vans if van.county ==
                               county_filter]

        self.assertEqual(len(response.context['vans']),
                         len(greater_london_vans))

        for van in greater_london_vans:
            self.assertIn(van, response.context['vans'])
