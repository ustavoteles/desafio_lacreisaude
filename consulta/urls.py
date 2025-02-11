from django.urls import path
from .views import (
    ConsultaListCreate,
    ConsultaRetrieveUpdateDestroy,
    ConsultaListByProfissional,
)

urlpatterns = [
        path('', ConsultaListCreate.as_view(), name='consulta-list-create'),
    path(
        "<int:pk>/",
        ConsultaRetrieveUpdateDestroy.as_view(),
        name="consulta-detail",
    ),
    path(
        "profissional/<int:profissional_id>/",
        ConsultaListByProfissional.as_view(),
        name="consulta-list-by-profissional",
    ),
]
