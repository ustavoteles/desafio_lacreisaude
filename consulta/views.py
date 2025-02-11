from django.forms import ValidationError
from rest_framework import generics
from rest_framework.response import Response

from .models import Consulta
from .serializers import ConsultaSerializer

from profissional.models import Profissional


def get_nome_profissional(profissional):
    return profissional.nome_social if profissional.nome_social else profissional.nome


class ConsultaListCreate(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer



class ConsultaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class ConsultaListByProfissional(generics.ListAPIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        profissional_id = self.kwargs.get("profissional_id")
        return Consulta.objects.filter(profissional_id=profissional_id).select_related(
            "profissional"
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        profissional = queryset.first().profissional if queryset.exists() else None
        nome_profissional = (
            get_nome_profissional(profissional) if profissional else None
        )
        return Response(
            {"nome_profissional": nome_profissional, "consultas": serializer.data}
        )
