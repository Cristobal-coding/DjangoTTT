from django.db import models
from applications.asignaturas.models import Asignatura
from applications.alumnos.models import Alumno
from .managers import CursoManager
# Create your models here.
class Fecha(models.Model):
    semestres=(
        ('1','Primer semestre'),
        ('2','Segundo semestre'),
    )
    years=(
        ('2021','2021'),('2020','2020'),('2019','2019'),
        ('2018','2018'),('2017','2017'),('2016','2016'),
        ('2015','2015'),('2014','2014'),('2013','2013'),
        ('2012','2012'),('2011','2011'),('2010','2010'),
        ('2009','2009'),('2008','2008'),('2007','2007'),
        ('2006','2006'),('2005','2005'),('2004','2004'),
        ('2003','2003'),('2002','2002'),('2001','2001'),
        ('2000','2000'),     
    )
    cod_fecha =models.CharField('Cod_fecha',max_length=5,unique=True,primary_key=True)    
    fecha_inicio=models.DateField('Fecha de inicio')
    fecha_termino=models.DateField('Fecha de Termino',null=True,blank=True)
    semestres=models.CharField('Semestre',max_length=3,choices=semestres)
    year=models.CharField('Año',max_length=4,choices=years)
    def __str__(self):
        return self.get_year_display()+ ' Semestre ' + self.semestres
    class Meta:
        unique_together = (('semestres', 'year'),)
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

class PlanEstudio(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    detalle_url = models.CharField('Url', max_length=255)
    asignaturas = models.ManyToManyField(Asignatura, through='Asignatura_Plan')
    def __str__(self):
        return self.nombre

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
    def __str__(self):
        return self.nombre +'('+self.id_curso + ')'
    id_curso =models.CharField('ID_Curso',max_length=20,unique=True,primary_key=True)
    cod_fecha=models.ForeignKey(Fecha,on_delete=models.CASCADE, related_name='curso')   
    nombre = models.CharField('Nombre', max_length=50)
    letra = models.CharField('Letra', max_length=1)
    electivo=models.CharField('Electivos',max_length=5,choices=electivos_choices, blank=True, null=True)

    objects = CursoManager()

    id_prof_jefe=models.ForeignKey(Profesor,on_delete=models.CASCADE, related_name='jefe')
    plan_estudio=models.ForeignKey(PlanEstudio,on_delete=models.CASCADE, related_name='plan')
    alumnos = models.ManyToManyField(Alumno,through='Curso_Alumno', related_name='cursos')

class Asignatura_Plan(models.Model):
    
    class Meta:
        db_table= 'Asignatura_Plan'
        unique_together = (('plan', 'asignatura'),)
    def __str__(self):
        return self.plan.nombre + ' '+self.asignatura.cod_asign
    #Clave primaria de m2m
    plan=models.ForeignKey(PlanEstudio,on_delete=models.CASCADE)
    asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)

    #foranea hacia profesores
    id_profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE,related_name='profesor')

class Curso_Alumno(models.Model):

    class Meta:
        db_table= 'Curso_Alumno'
        unique_together = (('curso', 'alumno'),)
    def __str__(self):
        return self.alumno.nombre + ' '+ self.curso.id_curso
    #Clave primaria de m2m
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE)

    #atributo si es curso actual
    is_current = models.BooleanField(default=False)