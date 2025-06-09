from django.conf import settings
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)  


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O e-mail do usuário deve ser informado.')

        usuario = self.model(
            # normaliza os emails deixando tudo em minusculo
            email=self.normalize_email(email), 
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(self._db)

        return usuario


    def create_superuser(self, email, password):
        usuario = self.create_user(email, password)
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)

        return usuario



class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True ,blank=False, null=False, 
                              help_text='O e-mail informado será utilizado para fazer o login no sistema.')
    nome = models.CharField(max_length=100)
    is_active = models.BooleanField(verbose_name='Ativo', default=True)
    is_staff = models.BooleanField(verbose_name='Administrador', default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"

    class Meta:
        db_table = 'usuario'


# ================================================================
# Outros Models
# ================================================================

class Receita(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=255)
    descricao = models.TextField(verbose_name='Descrição')
    tempo_preparo = models.IntegerField(verbose_name='Tempo de Preparo', help_text='Em minutos')
    preco = models.DecimalField(verbose_name='Preço', max_digits=7, decimal_places=2) 
    link = models.CharField(verbose_name='Link', max_length=255, blank=True)
    # obtem o usuario configurado neste projeto do arquivo settings.py
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        db_table = 'receita'

    # representacao deste objeto como uma STRING
    def __str__(self):
        return self.titulo


    # def save(self, *args, **kwargs):
    #     return super().save(*args, **kwargs)