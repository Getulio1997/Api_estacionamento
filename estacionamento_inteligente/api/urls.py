from django.urls import path
from .views.usuarioListView import UsuarioListView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="APIs",
      default_version='v1',
      description="Documentação da API da aplicação Estacionamento Inteligente",
   ),
)

urlpatterns = [
    path('usuarios', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/<int:id>/', UsuarioListView.as_view(), name='usuario_detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]
