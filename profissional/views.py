from rest_framework import generics
from .models import Profissional
from .serializers import ProfissionalSerializer
from rest_framework.filters import SearchFilter


class ProfissionalListCreate(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class ProfissionalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class ProfissionalListByNome(generics.ListAPIView):
    queryset = Profissional.objects.prefetch_related('consultas')  # Carrega as consultas junto com os profissionais
    serializer_class = ProfissionalSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']