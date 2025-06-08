"""
URL mapping para a API de gerenciamento de receitas
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from receita import views

# necessario para criar rotas automaticamente para os ViewSets
router = DefaultRouter()
# registra o ViewSet de receitas e mapeia os seus EndPoints para "receitas/"
# Como ReceitaViewSet eh um ModelViewSet, serao automaticamente mapeados 
# para os metodos HTTP (GET, PUT, PATCH, e DELETE)
router.register('receita', views.ReceitaViewSet)

# necessario para criar a funcao reversa
app_name = 'receita'

urlpatterns = [
    # inclui as URLs geradas automaticamente pelo objeto router
    path('', include(router.urls)),
]