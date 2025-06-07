"""
Views da API de gerenciamento de Usuarios
"""

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from usuario.serializers import (
    UsuarioSerializer,
    CriarTokenSerializer,
)


# CreateAPIView lida com POST resquests para criar objetos
class CriarUsuarioView(generics.CreateAPIView):
    """EndPoint para criar um novo usuario"""
    # define o serializer que sera utilizado para criar objetos
    serializer_class = UsuarioSerializer


class CriarTokenView(ObtainAuthToken):
    """EndPoint para criar um novo token de acesso para o usuario"""
    serializer_class = CriarTokenSerializer
    # opcional para exibir uma UI mais agradavel para testar a API
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# RetrieveUpdateAPIView lida com GET e PUT resquests para recuperar e alterar objetos
class GerenciarUsuarioView(generics.RetrieveUpdateAPIView):    
    """EndPoint para gerenciar usuarios: recuperar e alterar"""
    # define o serializer que sera utilizado 
    serializer_class = UsuarioSerializer

    # garante que o usuario autenticado tenha permissoes para executar esta API
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # sobrescreve o metodo para retornar o objeto Usuario para a View
    def get_object(self):
        """Obtem e retorna o usuario autenticado"""
        return self.request.user