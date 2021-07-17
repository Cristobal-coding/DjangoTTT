from applications.antecedentes.models import Antecedente
from django.db import models
from ckeditor.fields import RichTextField

from .managers import AlumnoManager, ApoderadoManager

class Apoderado(models.Model):
    rut =models.CharField('Rut',max_length=13,unique=True,primary_key=True)    
    nombre_apoderado=models.CharField('Nombre apoderado',max_length=50)
    apellido_paterno =models.CharField('Apellido paterno',max_length=25)
    apellido_materno =models.CharField('Apellido materno',max_length=25)
    telefono_apoderado=models.CharField('Telefono apoderado',max_length=8)
    correo=models.CharField('Correo',max_length=20, unique=True)

    objects = ApoderadoManager()

    def __str__(self):
        return self.nombre_apoderado+ ' ' + self.apellido_paterno+ ' ' + self.apellido_materno+'('+self.rut+')'
    class Meta:
        verbose_name = 'Apoderado'
        verbose_name_plural = 'Apoderados'
        db_table= 'Apoderados'
        ordering = ['nombre_apoderado','apellido_paterno']
        
class Alumno(models.Model):
    SEX_CHOICES = (
        ('0','Femenino'),
        ('1','Masculino'),
        ('2','No especifica')
    )
    ESTADO_CHOICES=(
        ('0','Regular'),
        ('1','Abandonó'),
        ('2','Graduado')
    )
    
    rut =models.CharField('Rut',max_length=13,unique=True,primary_key=True)
    nombre = models.CharField('Nombre',max_length=50,unique=False, null=True)
    apellido_paterno =models.CharField('Apellido paterno',max_length=25)
    apellido_materno =models.CharField('Apellido materno',max_length=25)
    fecha_nacimiento=models.DateField('Fecha de nacimiento',null=True,blank=True)
    sexo=models.CharField('Sexo',max_length=1,choices=SEX_CHOICES)
    telefono=models.CharField('Telefono',max_length=8,null=True,blank=True)
    direccion=models.CharField('Direccion',max_length=50,null=True,blank=True)
    estado=models.CharField('estado',max_length=1,choices=ESTADO_CHOICES,blank=False)

    rut_apoderado=models.ForeignKey(Apoderado,on_delete=models.CASCADE,max_length=13,unique=False, related_name='alumnos')
    antecedentes = models.ManyToManyField(Antecedente, through='Alumno_antecedente')

    objects = AlumnoManager()
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        db_table= 'Alumnos'
        ordering=['apellido_paterno','apellido_materno']
    def __str__(self):
        return self.nombre + ' - ' + self.rut

    def get_current_curso(self):
        cursos = self.curso_alumno_set.all()
        cursando = False
        
        if len(cursos) > 0 :
            for c in cursos:
                if c.is_current :
                    cursando = True
                    nombre=c.curso.nombre
        if cursando :
            return nombre
        elif self.estado == '0':
            return 'Sin Curso'
        elif self.estado == '2':
            return 'Graduado'
        else:
            return 'No Cursando'


class Alumno_antecedente(models.Model):
    class Meta:
        db_table= 'Alumno_antecedente'
        unique_together = (('alumno', 'antecedente'),)
    def __str__(self):
        return str(self.alumno.rut) + ' '+ str(self.antecedente_id)
    #Clave primaria de m2m
    alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE)
    antecedente=models.ForeignKey(Antecedente,on_delete=models.CASCADE)
    #atributos
    fecha=models.DateField('Fecha')
    detalle=RichTextField()
    # detalle=models.CharField(max_length=255,blank=True)

  