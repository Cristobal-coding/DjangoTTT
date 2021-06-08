from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class Rol(models.Model):
    nombre = models.CharField(max_length=50,unique=True,error_messages={'unique':"Ya existe un rol con este Nombre."})
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table= 'Roles'


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username',max_length=20)
    rut = models.CharField('Rut',max_length=13,blank=True, unique=True,error_messages={'unique':"Este Rut ya esta Registrado."})
    image = models.ImageField( upload_to='usuarios', blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True , null=True ,related_name='usuarios')
    activo = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['username']
    objects= UserManager()

    def __str__(self):
        return self.username + ' ' + self.rut
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table= 'Usuarios'
        ordering=['username']

