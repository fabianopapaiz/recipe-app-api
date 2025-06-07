"""
URL mapping para a API de gerenciamento de usuarios
"""

from django.urls import path

from usuario import views

# necessario para criar a funcao reversa
app_name = 'usuario'

urlpatterns = [
    path(
        # qualquer URL com esse padrao sera tratado pela view especificada
        'criar/',
        views.CriarUsuarioView.as_view(),
        # o metodo chamado sera o 'UsuarioView.UsuarioSerializer.criar()'
        name='criar',
    ),
    path(
        # qualquer URL com esse padrao sera tratado pela view especificada
        'token/',
        views.CriarTokenView.as_view(),
        # o metodo chamado sera o 'UsuarioView.UsuarioSerializer.criar()'
        name='token',
    ),
    path(
        # qualquer URL com esse padrao sera tratado pela view especificada
        'perfil/',
        views.GerenciarUsuarioView.as_view(),
        # o metodo chamado sera o 'UsuarioView.UsuarioSerializer.criar()'
        name='perfil',
    ),

]