from django.db import models

# Create your models here.

class PlanEstudio(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    detalle_url = models.CharField('Url', max_length=255)
    # asignaturas = models.ManyToManyField(Asignatura, through='Asignatura_Plan', related_name='plan')
    def __str__(self):
        return self.nombre + ' ' + str(self.id)
        
class Asignatura(models.Model):
    cod_asign =models.CharField('Cod_asign',max_length=4,unique=True,primary_key=True)     
    nombre=models.CharField('Nombre',max_length=30)
    plan=models.ForeignKey(PlanEstudio,on_delete=models.CASCADE,related_name='asignaturas', null=True, blank=True)
    

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        db_table= 'Asignaturas'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre+ '( ' + self.cod_asign + ')'