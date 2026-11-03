from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_is_available(self):
        response = self.client.get(reverse('academia:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Seu projeto está pronto para começar.')
        self.assertContains(response, 'é necessário entrar com uma conta administradora')
        self.assertContains(
            response,
            f'href="{reverse("admin:index")}"',
        )

    def test_admin_requires_login(self):
        response = self.client.get(reverse('admin:index'))

        self.assertRedirects(
            response,
            f'{reverse("admin:login")}?next={reverse("admin:index")}',
            fetch_redirect_response=False,
        )
