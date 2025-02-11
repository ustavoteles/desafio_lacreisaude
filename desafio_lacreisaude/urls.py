from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Desafio Backend Lacrei Saúde API",
        default_version="v1",
        description="API para gerenciamento de consultas médicas e profissionais de saúde",
        contact=openapi.Contact(email="telesgustavo.dev@gmail.com"),
    ),
    public=True,
)

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/swagger/')),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
    path("api/profissionais/", include("profissional.urls")),
    path("api/consultas/", include("consulta.urls")),
    
]
