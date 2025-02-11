from rest_framework import serializers

from .models import Profissional
from .models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    profissional_nome = serializers.CharField(source='profissional.nome', read_only=True)

    class Meta:
        model = Consulta
        fields = "__all__"
        extra_fields = ['profissional']
