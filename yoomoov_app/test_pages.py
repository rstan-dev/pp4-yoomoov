from django.test import TestCase, override_settings
from django.urls import reverse, path
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponseServerError
from .models import Van, Booking, Feedback
from datetime import date, datetime


class HomePageTest(TestCase):
    # Test for an accessbile page, correct template and the latest
    # 3 van listings are displaying correctly

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
        self.assertTemplateUsed(response, 'pages/index.html')

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
        self.assertTemplateUsed(response, 'pages/services.html')


class VanDetailViewTest(TestCase):
    # Test for successful retrieval of van detail page based on a valid slug.
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
        self.assertTemplateUsed(response, 'pages/van_detail.html')

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
    # Tests if van search results display vans according to selected filters,

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
        self.assertTemplateUsed(response, 'pages/van_filter.html')

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
