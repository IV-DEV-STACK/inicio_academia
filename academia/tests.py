from django.test import TestCase
from django.urls import reverse

from academia.models import Plano

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


class PlanoApiTests(TestCase):
    def test_plano_list_endpoint_is_available(self):
        response = self.client.get(reverse('academia:plano-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_plano_can_be_created_through_api(self):
        response = self.client.post(
            reverse('academia:plano-list'),
            {
                'nome': 'Mensal',
                'descricao': 'Acesso mensal',
                'duracao_dias': 30,
                'valor': '99.90',
                'ativo': True,
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Plano.objects.count(), 1)
        self.assertEqual(Plano.objects.get().nome, 'Mensal')
