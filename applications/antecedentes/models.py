from django.db import models



# Create your models here.


class Antecedente(models.Model):
    nombre_antecedente=models.CharField('Nombre antecedente',max_length=50)
    def __str__(self):
        return str(self.id)+ ' Nombre antecedente ' + self.nombre_antecedente
    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'
        db_table= 'Antecedentes'
        ordering = ['id']




