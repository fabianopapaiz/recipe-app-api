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
    email = models.EmailField(max_length=255, unique=True ,blank=False, null=False)
    nome = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"

    class Meta:
        db_table = 'usuario'