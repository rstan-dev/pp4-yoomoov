from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.test import Client
from django.http import HttpResponseServerError
from .models import Van
from datetime import date, datetime
from django.utils import timezone


class ContactFormTest(TestCase):
    # Tests the contact form submits a POST request correctly
    # and displays a success message after form is submitted.  Also checks
    # for if there is a slug, and if so the redirect should be back to the
    # van page or redirect to the home page.

    def setUp(self):
        # Creates a Van Object to test contact form with slug
        date_added_3 = timezone.datetime(2024, 1, 2, 12, 0)

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
        self.assertTemplateUsed(response, 'contact/contact.html')

    # Test to ensure the POST request is successful and a success
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

    # Test to check contact form redirects back to home page if no slug
    # is present
    def test_contact_form_no_slug_redirects_to_home(self):
        response = self.client.post(reverse('contact'), self.form_data)
        self.assertRedirects(response, reverse('home'))
