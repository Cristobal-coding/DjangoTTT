from django.db import models
# Create your models here.
from applications.asignaturas.models import Asignatura
from applications.alumnos.models import Alumno
# Create your models here.
class Psicologo(models.Model):
    nombre=models.CharField('Nombre',max_length=50)
    apellido_paterno =models.CharField('Apellido paterno',max_length=30)
    apellido_materno =models.CharField('Apellido materno',max_length=30)
    correo=models.CharField('Correo',max_length=50, unique=True)
    telefono=models.CharField('Telefono',max_length=8)
    fecha_ingreso=models.DateField('Fecha de ingreso')
    def __str__(self):
        return str(self.id)+ ' '+ self.nombre + ' ' + self.apellido_paterno
    class Meta:
        verbose_name = 'Psicologo'
        verbose_name_plural = 'Psicologos'
        db_table= 'Psicologos'
        ordering = ['id']

class Informe(models.Model):
    fecha_emision=models.DateField('Fecha de emision')
    pruebas_aplicadas=models.CharField('Pruebas aplicadas',max_length=255)
    motivo=models.CharField('Motivo',max_length=255,blank=True)
    comentario=models.CharField('Comentario',max_length=255,blank=True)
    id_psicologo=models.ForeignKey(Psicologo,on_delete=models.CASCADE,related_name='informes')
    rut_alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE,related_name='informes')
    class Meta:
        verbose_name = 'Informe'
        verbose_name_plural = 'Informes'
        db_table= 'Informes'  
        ordering = ['-fecha_emision','-id']
    def __str__(self):
        return str(self.fecha_emision) +'(Nombre del alumno. '+self.rut_alumno.nombre +' '+  self.rut_alumno.apellido_paterno+')'
    

