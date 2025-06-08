"""
Views para a API de gerenciamento de receitas
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import Receita
from receita import serializers


class ReceitaViewSet(viewsets.ModelViewSet):
    """View para gerenciar API de receitas"""

    # define o serializer que sera utilizado 
    serializer_class = serializers.ReceitaSerializer
    # objeto QuerySet para gerenciar os dados do model
    queryset = Receita.objects.all()

    # define que todos os EndPoints exigem uma autenticacao via Token
    # e, dessa forma, que o usuario esteja autenticado
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Sobrescreve o queryset por um filtrado pelo usuario autenticado
    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user).order_by('-id')
