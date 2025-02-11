from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.utils.timezone import now
from profissional.models import Profissional


class Consulta(models.Model):
    data_consulta = models.DateTimeField(default=timezone.now)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE,related_name='consultas')

    class Meta:
        db_table = "consulta"

    def __str__(self):
        nome = (
            self.profissional.nome_social
            if self.profissional.nome_social
            else self.profissional.nome
        )
        return f"Consulta com {nome} em {self.data_consulta.strftime('%d/%m/%Y %H:%M')}"

    def clean(self):
        if self.data_consulta < timezone.now():
            raise ValidationError("A data da consulta não pode ser no passado.")
