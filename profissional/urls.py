from django.urls import path
from .views import (
    ProfissionalListByNome,
    ProfissionalListCreate,
    ProfissionalRetrieveUpdateDestroy,
)

urlpatterns = [
    path(
        "",
        ProfissionalListCreate.as_view(),
        name="profissional-list-create",
    ),
    path(
        "<int:pk>/",
        ProfissionalRetrieveUpdateDestroy.as_view(),
        name="profissional-detail",
    ),
    path(
        "nome/",
        ProfissionalListByNome.as_view(),
        name="profissional-by-nome",
    ),
]
