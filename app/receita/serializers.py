"""
Serializers para a API de gerenciamento de receitas
"""

from django.contrib.auth import get_user_model

# utilitario para traducao de idiomas
from django.utils.translation import gettext as _

from rest_framework import serializers

from core.models import Receita


class ReceitaSerializer(serializers.ModelSerializer):
    """ Serializer para o objeto Receita """

    class Meta:
        model = Receita
        fields = ['id', 'titulo', 'descricao',  'tempo_preparo',  'preco',  'link']
        read_only_fields = ['id']


    def create(self, validated_data):
        receita = Receita.objects.create(**validated_data)
        return receita


# def ReceitaDetalheSerializer(ReceitaSerializer):
#     """ Serializer para exibir os detalhes de uma Receita, herdando de ReceitaSerializer"""

#     # herda o Meta da superclasse
#     class Meta(ReceitaSerializer.Meta):
#         # adiciona o campo descricao
#         fields = ReceitaSerializer.Meta.fields + ['descricao']


#     def create(self, validated_data):
#         print('ReceitaDetalheSerializer.create()')
#         return super().create(self, validated_data)
