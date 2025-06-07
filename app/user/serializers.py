"""
Serializers para a API de generiamento de usuarios
"""

from django.contrib.auth import get_user_model

from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    """ Serializer para o objeto Usuario """

    class Meta:
        # obtem o model do user definido neste projeto
        model = get_user_model()
        # define o conjunto de campos que serao disponibilizados via serializacao
        # os quais serao usados, por exemplo, para criar um novo usuario
        fields = ['email', 'password', 'nome']
        # defineicoes extra para os campos definidos anteriormente
        extra_kwargs = {
            'password': {
                # sera apenas para escrita e seu valor nao sera enviado na resposta
                'write_only': True,
                # tamanho minimo aceito para a senha (validacao)
                'min_length': 5,
            }
        }

    def create(self, validated_data):
        """Cria e retorna um Usuario com a senha criptografada"""
        return get_user_model().objects.create_user(**validated_data)    