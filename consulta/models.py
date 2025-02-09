from django.db import models
from profissional.models import Profissional


# Create your models here.
class Consulta(models.Model):
    data = models.DateTimeField()
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)

    def __str__(self):
        nome = (
            self.profissional.nome_social
            if self.profissional.nome_social
            else self.profissional.nome
        )
        return f"Consulta com {self.profissional.nome} em {self.data}"
