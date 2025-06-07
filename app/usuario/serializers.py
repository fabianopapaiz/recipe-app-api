"""
Serializers para a API de generiamento de usuarios
"""

from django.contrib.auth import (
    get_user_model,
    authenticate,
)

# utilitario para traducao de idiomas
from django.utils.translation import gettext as _

from rest_framework import serializers


# cria um serializer que sera baseado em um Model existente
class UsuarioSerializer(serializers.ModelSerializer):
    """ Serializer para o objeto Usuario """

    class Meta:
        # obtem o model a ser utilizado neste serializer
        model = get_user_model() # user-model definido neste projeto
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


    # OBS: tem que usar "create" para sobrescrever o metodo padrao  
    def create(self, validated_data):
        """Cria e retorna um Usuario com a senha criptografada"""
        return get_user_model().objects.create_user(**validated_data)    


    # OBS: tem que usar "update" para sobrescrever o metodo padrao  
    def update(self, instance, validated_data):
        """Altera e retorna os dados de um Usuario existente"""

        # obtem a nova senha, caso ela tenha sido informada.
        # Se nao tiver sido informada irah retornar None.
        # o metodo pop() irah obter e remover os dados da senha em validated_data
        password = validated_data.pop('password', None)

        # Alterar os dados (menos a senha) chamando o metodo update() padrao do Model
        usuario = super().update(instance, validated_data)

        # Altera a senha caso ela tenha sido informada uma nova senha
        if password:
            usuario.set_password(password)
            usuario.save()

        return usuario


# cria um serializer PADRAO, i.e., que NAO eh baseado em um Model
class CriarTokenSerializer(serializers.Serializer):            
    """ Serializer para autenticacao de usuarios via TOKEN """

    # define os campos necessarios
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    # este metodo sera chamado no estagio de validacao a partir da view, a qual
    # passarah os dados para o serializer verificar se os dados estao corretos
    def validate(self, attrs):
        """Valida os dados de autenticacao do usuario"""

        # obtem os parametros informados
        email = attrs.get('email')
        password = attrs.get('password')

        # tenta autenticar o usuario
        usuario = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
 
        # se nao conseguiu autenticar lanca um erro
        if not usuario:
            raise serializers.ValidationError(
                'Não foi possível autenticar o usuário com as credenciais fornecidas.',
                code='authorization',
            )
        # se o usuario foi autenticado com sucesso
        else:
            # adiciona o usuario autenticado nos parametros e retorna 
            # OBS: tem que usar "user" para funcionar   
            attrs['user'] = usuario
            return attrs

