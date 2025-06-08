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


