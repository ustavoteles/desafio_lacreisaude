from django.db import models
from django.forms import ValidationError
from django.core.validators import EmailValidator



# Create your models here.
class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, default="")
    nome_social = models.CharField(max_length=100, default="", blank=True, null=True)
    profissao = models.CharField(max_length=100, default="")
    contato = models.CharField(
        max_length=100, default="", validators=[EmailValidator()]
    )
    endereco = models.CharField(max_length=100, default="")


    class Meta:
        db_table = "profissional"

    def clean(self):
        if self.nome_social == self.nome:
            raise ValidationError(
                "O nome social não pode ser o mesmo que o nome completo."
            )

    def __str__(self):

        return (
            f"ID: {self.id} | Nome: {self.nome} | Nome Social: {self.nome_social} | "
            f"Profissão: {self.profissao} | Contato: {self.contato} | "
            f"Endereço: {self.endereco}"
        )
