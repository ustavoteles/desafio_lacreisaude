from rest_framework.test import APITestCase
from rest_framework import status


class ProfissionalAPITestCase(APITestCase):
    def setUp(self):
        self.profissional_data = {
            "nome": "Dr. Gustavo",
            "profissao": "Cardiologista",
            "contato": "gustavo@email.com",
            "endereco": "Av. Paulista, 1234",
        }

    def test_create_profissional(self):
        """
        Teste para criar um profissional através de API.
        """
        response = self.client.post(
            "/api/profissionais/", self.profissional_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], self.profissional_data["nome"])
