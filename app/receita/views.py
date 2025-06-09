"""
Views para a API de gerenciamento de receitas
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import Receita
from receita import serializers

# CODIGO QUE ESTAVA ANTES DE INCLUIR O RECETA-DETALHE 
# class ReceitaViewSet(viewsets.ModelViewSet):
#     """View para gerenciar API de receitas"""

#     # define o serializer que sera utilizado 
#     serializer_class = serializers.ReceitaSerializer
#     # objeto QuerySet para gerenciar os dados do model
#     queryset = Receita.objects.all()

#     # define que todos os EndPoints exigem uma autenticacao via Token
#     # e, dessa forma, que o usuario esteja autenticado
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     # Sobrescreve o queryset por um filtrado pelo usuario autenticado
#     def get_queryset(self):
#         return self.queryset.filter(usuario=self.request.user).order_by('-id')


class ReceitaViewSet(viewsets.ModelViewSet):
    """View para gerenciar API de receitas"""

    # define o serializer que sera utilizado. Aqui foi usado o
    # ReceitaDetalhe ao inves de Receita porque a mairia dos metodos
    # utilizados estarao em ReceitaDetalhe (incluir, alterar, excluir) 
    serializer_class = serializers.ReceitaSerializer
    # objeto QuerySet para gerenciar os dados do model
    queryset = Receita.objects.all()

    # define que todos os EndPoints exigem uma autenticacao via Token
    # e, dessa forma, que o usuario esteja autenticado
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Sobrescreve o queryset por um filtrado pelo usuario autenticado
    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user).order_by('titulo')

    # # sobrescreve o metodo para obter o serializer
    # def get_serializer_class(self):
    #     # se a acao for 'list' (listagem) retorna o serializer Receita
    #     if self.action == 'list':
    #         print('get_serializer_class = ReceitaSerializer')
    #         return serializers.ReceitaSerializer
    #     # se for outra acao, retorna o serializer ReceitaDetalhe
    #     else:
    #         print('get_serializer_class = ReceitaDetalheSerializer')
    #         return self.serializer_class

    def perform_create(self, serializer):
        """Cria uma nova receita"""
        print('ReceitaViewSet.perform_create()')

        # cria uma nova receita informando o usuario autenticado
        serializer.save(usuario=self.request.user)

