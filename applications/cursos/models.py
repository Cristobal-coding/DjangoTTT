from django.db import models
from applications.asignaturas.models import Asignatura
from applications.alumnos.models import Alumno
# Create your models here.
class Fecha(models.Model):
    semestres=(
        ('1','Primer semestre'),
        ('2','Segundo semestre'),
    )
    años=(
        ('0','2021'),('1','2020'),('2','2019'),
        ('3','2018'),('4','2017'),('5','2016'),
        ('6','2015'),('7','2014'),('8','2013'),
        ('9','2012'),('10','2011'),('11','2010'),
        ('12','2009'),('13','2008'),('14','2007'),
        ('15','2006'),('16','2005'),('17','2004'),
        ('18','2003'),('19','2002'),('20','2001'),
        ('21','2000'),     
    )
    cod_fecha =models.CharField('Cod_fecha',max_length=5,unique=True,primary_key=True)    
    fecha_inicio=models.DateField('Fecha de inicio')
    fecha_termino=models.DateField('Fecha de Termino',null=True,blank=True)
    semestres=models.CharField('Semestre',max_length=3,choices=semestres)
    año=models.CharField('Año',max_length=4,choices=años)
    def __str__(self):
        return self.get_año_display()+ ' Semestre ' + self.semestres
    class Meta:
        unique_together = (('semestres', 'año'),)
        verbose_name = 'Fecha'
        verbose_name_plural = 'Fechas'
        db_table= 'Fechas'
        # ordering = ['nombre_apoderado','apellido_paterno']
class Profesor(models.Model):
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        db_table= 'Profesores'  
        ordering = ['nombres']
    def __str__(self):
        return self.nombres +'(Prof. '+self.asig_impartir.nombre + ')'
    nombres=models.CharField('Nombres',max_length=50)
    apellido_paterno=models.CharField('A.Paterno',max_length=30)
    apellido_materno=models.CharField('A.Materno',max_length=30)
    asig_impartir=models.ForeignKey(Asignatura,on_delete=models.CASCADE, related_name='asignatura')

class Curso(models.Model):
    electivos_choices=(
        ('EL','Electricidad'),
        ('MET','Construcciones metálicas.'),
        ('CON','Construccion'),
    )  
    class Meta:
        unique_together = (('id_curso', 'cod_fecha'),)
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        db_table= 'Cursos'
        ordering = ['nombre']
    id_curso =models.CharField('ID_Curso',max_length=20,unique=True,primary_key=True)
    cod_fecha=models.ForeignKey(Fecha,on_delete=models.CASCADE, related_name='fecha')   
    nombre = models.CharField('Nombre', max_length=50)
    letra = models.CharField('Letra', max_length=1)
    electivo=models.CharField('Electivos',max_length=5,choices=electivos_choices, blank=True, null=True)
    id_prof_jefe=models.ForeignKey(Profesor,on_delete=models.CASCADE, related_name='jefe')
    asignaturas = models.ManyToManyField(Asignatura, through='Asignatura_Curso')
    alumnos = models.ManyToManyField(Alumno)

class Asignatura_Curso(models.Model):

    class Meta:
        db_table= 'Asignatura_Curso'
        unique_together = (('curso', 'asignatura'),)
    def __str__(self):
        return self.curso.id_curso + ' '+self.asignatura.cod_asign
    #Clave primaria de m2m
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)

    #foranea hacia profesores
    id_profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE,related_name='profesor')