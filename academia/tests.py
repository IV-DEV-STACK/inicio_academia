from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_is_available(self):
        response = self.client.get(reverse('academia:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Seu projeto está pronto para começar.')
