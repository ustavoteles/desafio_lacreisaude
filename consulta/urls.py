from django.urls import path
from .views import (
    ConsultaListCreate,
    ConsultaRetrieveUpdateDestroy,
    ConsultaListByProfissional,
)

urlpatterns = [
    path("consultas/", ConsultaListCreate.as_view(), name="consulta-list-create"),
    path(
        "consultas/<int:pk>/",
        ConsultaRetrieveUpdateDestroy.as_view(),
        name="consulta-detail",
    ),
    path(
        "consultas/profissional/<int:profissional_id>/",
        ConsultaListByProfissional.as_view(),
        name="consulta-list-by-profissional",
    ),
]
