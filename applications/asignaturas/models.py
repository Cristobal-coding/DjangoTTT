from django.db import models

# Create your models here.
class Asignatura(models.Model):
    cod_asign =models.CharField('Cod_asign',max_length=4,unique=True,primary_key=True)     
    nombre=models.CharField('Nombre',max_length=30)
    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        db_table= 'Asignaturas'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre+ '( ' + self.cod_asign + ')'