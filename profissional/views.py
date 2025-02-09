from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profissional
from .serializers import ProfissionalSerializer


class ProfissionalListCreate(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class ProfissionalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class ProfissionalListByNome(generics.ListAPIView):
    serializer_class = ProfissionalSerializer
