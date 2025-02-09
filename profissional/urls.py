from django.urls import path
from .views import (
    ProfissionalListCreate,
    ProfissionalRetrieveUpdateDestroy,
)

urlpatterns = [
    path(
        "profissionais/",
        ProfissionalListCreate.as_view(),
        name="profissional-list-create",
    ),
    path(
        "profissionais/<int:pk>/",
        ProfissionalRetrieveUpdateDestroy.as_view(),
        name="profissional-detail",
    ),
    # path(
    #     "update/<int:id>/", update_profissional_by_id, name="update-profissional-by-id"
    # ),
]
