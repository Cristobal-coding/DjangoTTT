from django.db import models
from .managers import AlumnoManager

class Apoderado(models.Model):
    rut =models.CharField('Rut',max_length=13,unique=True,primary_key=True)    
    nombre_apoderado=models.CharField('Nombre apoderado',max_length=50)
    apellido_paterno =models.CharField('Apellido paterno',max_length=25)
    apellido_materno =models.CharField('Apellido materno',max_length=25)
    telefono_apoderado=models.CharField('Telefono apoderado',max_length=8)
    correo=models.CharField('Correo',max_length=20)
    def __str__(self):
        return self.nombre_apoderado+ ' ' + self.apellido_paterno+ ' ' + self.apellido_materno+'('+self.rut+')'
    class Meta:
        verbose_name = 'Apoderado'
        verbose_name_plural = 'Apoderados'
        db_table= 'Apoderados'
class Alumno(models.Model):
    SEX_CHOICES = (
        ('0','Femenino'),
        ('1','Masculino'),
        ('2','No especifica')
    )
    ESTADO_CHOICES=(
        ('0','Regular'),
        ('1','Abandonó'),
        ('2','Finalizado')
    )
    rut =models.CharField('Rut',max_length=13,unique=True,primary_key=True)
    nombre = models.CharField('Nombre',max_length=50,unique=False)
    apellido_paterno =models.CharField('Apellido paterno',max_length=25)
    apellido_materno =models.CharField('Apellido materno',max_length=25)
    fecha_nacimiento=models.DateField('Fecha de nacimiento')
    rut_apoderado=models.ForeignKey(Apoderado,on_delete=models.CASCADE,max_length=13,unique=False)
    sexo=models.CharField('Sexo',max_length=1,choices=SEX_CHOICES)
    telefono=models.CharField('Telefono',max_length=8)
    direccion=models.CharField('Direccion',max_length=50)
    estado=models.CharField('estado',max_length=1,choices=ESTADO_CHOICES)

    objects = AlumnoManager()

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        db_table= 'Alumnos'
    def __str__(self):
        return self.nombre + ' - ' + self.rut
