from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as transl
from core import models


class UsuarioAdmin(UserAdmin):
    # define a ordenacao default dos registros
    ordering = ['email']
    # define os campos que serao exibidos na tela de listagem
    list_display = ['email', 'nome', 'is_active', 'is_staff', 'last_login']
    # define os campos somente de leitura
    readonly_fields = ['last_login']
    # define os campos que serao editados durante a inclusao ou alteracao.
    # Aqui tambem podem ser definidos grupos para agrupar campos
    fieldsets = (
        (
            None, # None = "Sem agrupamento"
            {'fields': ('email', 'password')},
        ),
        (
            transl('Permissões'), # Nome do grupo de campos, usando metodo para fazer traducao
            {'fields': ('is_active', 'is_staff', 'is_superuser')},
        ),
        (
            transl('Outras Informações'), # Nome do grupo de campos, usando metodo para fazer traducao
            {'fields': ('last_login',)},
        ),
    )
    # define os campos utilizados na tela de inclusao
    add_fieldsets = (
        (
            # None = "Sem agrupamento"
            'Dados de Acesso', 
            {   
                # defincao das classes CSS para serem aplicadas
                'classes': (
                    'wide', # wide: insere um espacamento horizontal extra entre os elementos
                    # 'collapse', # collapse: o grupo aparece 'recolhido' e o usuario podera expandir se quiser
                    # 'your_custom_css_class', # pode utilizar outras classes definidas em CSS
                ),
                # campos
                'fields': (
                    'email', 
                    'password1', # senha
                    'password2', # confirmação da senha
                )
            },
        ),
        (
            transl('Permissões'), # Nome do grupo de campos, usando metodo para fazer traducao
            {
                # pode ser inserida uma breve explicacao sobre o grupo de campos
                'description': ('Defina aqui as permissões de acesso deste usuário.'),
                # campos do grupo
                'fields': (
                    'is_active', 
                    'is_staff', 
                    'is_superuser'
                    )
                },
        ),
    )

admin.site.register(models.Usuario, UsuarioAdmin)