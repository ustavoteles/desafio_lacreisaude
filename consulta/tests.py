from .models import Consulta, Profissional
from django.utils import timezone
from rest_framework.test import APITestCase


class ConsultaAPITestCase(APITestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome="Dr. Gustavo",
            nome_social="Dr. Gustavo Silva",
            profissao="Cardiologista",
            contato="gustavo@email.com",
            endereco="Av. Paulista, 1234",
        )
        self.consulta = Consulta.objects.create(
            profissional=self.profissional,
            data_consulta=timezone.now(),
        )

    def test_consulta_profissional(self):
        # Este teste verifica se a consulta está corretamente associada ao profissional
        self.assertEqual(self.consulta.profissional, self.profissional)

