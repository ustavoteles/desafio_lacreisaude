from django.db import models


# Create your models here.
class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, default="")
    nome_social = models.CharField(max_length=100, default="", blank=True, null=True)
    profissao = models.CharField(max_length=100, default="")
    contato = models.CharField(max_length=100, default="")
    endereco = models.CharField(max_length=100, default="")

    def __str__(self):
        return (
            f"ID: {self.id} | Nome: {self.nome} | Nome Social: {self.nome_social} | "
            f"Profissão: {self.profissao} | Contato: {self.contato} | "
            f"Endereço: {self.endereco}"
        )
