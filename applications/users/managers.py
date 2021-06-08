from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username,rut, password, is_staff, is_superuser,**extra_fields):
        user = self.model(
            username=username,
            rut=rut,
            is_staff=is_staff,
            is_superuser=is_superuser,
            activo=False,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self, username, rut,password=None,**extra_fields):
        return self._create_user(username,rut, password,False,False,**extra_fields)

    def create_superuser(self, username,rut,password=None, **extra_fields):
        return self._create_user(username, rut,password,True, True,**extra_fields)