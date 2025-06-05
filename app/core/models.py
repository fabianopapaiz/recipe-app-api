from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)  


class UsuarioManager(BaseUserManager):

    def create_usuario(self, email, password=None, **extra_fields):
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(self._db)

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True,blank=False, null=False)
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    administrador = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"

    class Meta:
        db_table = 'usuario'