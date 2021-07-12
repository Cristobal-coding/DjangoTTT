from django.db import models
from applications.alumnos.models import Alumno
# Create your models here.

class PlanEstudio(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    detalle_url = models.CharField('Url', max_length=255)
    # asignaturas = models.ManyToManyField(Asignatura, through='Asignatura_Plan', related_name='plan')
    def __str__(self):
        return self.nombre + ' ' + str(self.id)
        
class Asignatura(models.Model):
    cod_asign =models.CharField('Cod_asign',max_length=4,unique=True,primary_key=True)     
    nombre=models.CharField('Nombre',max_length=100)
    plan=models.ForeignKey(PlanEstudio,on_delete=models.CASCADE,related_name='asignaturas', null=True, blank=True)
    

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        db_table= 'Asignaturas'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre+ '( ' + self.cod_asign + ')'
class Parciales(models.Model):
    
    fecha = models.DateField('Fecha del parcial')
    calificacion = models.FloatField()
    alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE,related_name='parciales')
    asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE,related_name='parciales')
    

    class Meta:
        verbose_name = 'Parcial'
        verbose_name_plural = 'Parciales'
        db_table= 'Paraciales'
        ordering = ['id', 'fecha']
    def __str__(self):
        return str(self.calificacion)+ '( ' + self.asignatura.nombre + ')'