from django.test import TestCase, override_settings
from django.urls import reverse, path
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponseServerError
from .models import Van, Booking, Feedback
from datetime import date, datetime
from django.utils import timezone


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
        date_added_1 = timezone.datetime(2024, 1, 2, 12, 0)
        date_added_2 = timezone.datetime(2024, 2, 2, 12, 0)
        date_added_3 = timezone.datetime(2024, 3, 2, 12, 0)

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
