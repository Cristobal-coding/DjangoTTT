from applications.cursos.models import Fecha
from applications.alumnos.models import Alumno
from django.db import models

# Create your models here.

class Tipo(models.Model):
    nombre_tipo=models.CharField('Nombre tipo',max_length=50)
    def __str__(self):
        return str(self.id)+ ' Nombre tipo ' + self.nombre_tipo
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table= 'Tipos'
        ordering = ['id']

class Antecedente(models.Model): 
    cod_fecha=models.ForeignKey(Fecha,on_delete=models.CASCADE,related_name='antecedentes')
    rut_alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE,related_name='antecedentes',null=True,blank=True)
    dias_ausente=models.IntegerField('Dias ausente')
    antecedentes = models.ManyToManyField(Tipo, through='Antecedente_tipo')
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'
        db_table= 'Antecedentes'
        ordering = ['id']


class Antecedente_tipo(models.Model):
    class Meta:
        db_table= 'Antecedente_tipo'
        unique_together = (('antecedente', 'tipo'),)
    def __str__(self):
        return str(self.antecedente.id) + ' '+ str(self.tipo_id)
    #Clave primaria de m2m
    antecedente=models.ForeignKey(Antecedente,on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipo,on_delete=models.CASCADE)
    detalle=models.CharField(max_length=255,blank=True)

  
