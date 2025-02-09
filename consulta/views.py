from rest_framework import generics
from .models import Consulta
from .serializers import ConsultaSerializer


class ConsultaListCreate(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class ConsultaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class ConsultaListByProfissional(generics.ListAPIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        profissional_id = self.kwargs["profissional_id"]
        return Consulta.objects.filter(profissional_id=profissional_id)
