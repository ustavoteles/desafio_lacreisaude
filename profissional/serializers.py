from rest_framework import serializers

from consulta.serializers import ConsultaSerializer

from .models import Profissional


class ProfissionalSerializer(serializers.ModelSerializer):
    consultas = ConsultaSerializer(many=True, read_only=True)
    class Meta:
        model = Profissional
        fields = "__all__"