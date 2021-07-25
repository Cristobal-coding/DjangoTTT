
from django.db import models
from applications.asignaturas.models import Asignatura, PlanEstudio
from applications.alumnos.models import Alumno
from .managers import CursoManager,ProfesorManager, FechaManager
# Create your models here.

class Fecha(models.Model):
    semestres=(
        ('1','Primer semestre'),
        ('2','Segundo semestre'),
    )
    cod_fecha =models.CharField('Cod_fecha',max_length=5,unique=True,primary_key=True)    
    fecha_inicio=models.DateField('Fecha de inicio')
    fecha_termino=models.DateField('Fecha de Termino',null=True,blank=True)
    semestres=models.CharField('Semestre',max_length=3,choices=semestres)
    year= models.IntegerField('Año')
    objects = FechaManager()
    def __str__(self):
        return str(self.year)+ ' Semestre ' + self.semestres
    class Meta:
        unique_together = (('semestres', 'year'),)
        verbose_name = 'Fecha'
        verbose_name_plural = 'Fechas'
        db_table= 'Fechas'
        ordering = ['-year','-semestres']
class Profesor(models.Model):
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        db_table= 'Profesores'  
        ordering = ['nombres']
    def __str__(self):
        if (self.asig_impartir is not None):
            asign=self.asig_impartir.nombre
        else:
            asign="Sin Asignatura"
        return self.nombres +'(Prof. '+ asign + ')'
    rut=models.CharField('Rut',max_length=13,unique=True,primary_key=True)
    nombres=models.CharField('Nombres',max_length=50)
    apellido_paterno=models.CharField('A.Paterno',max_length=30,blank=True,null=True)
    apellido_materno=models.CharField('A.Materno',max_length=30,blank=True,null=True)
    asig_impartir=models.ForeignKey(Asignatura,on_delete=models.CASCADE, related_name='asignatura',blank=True,null=True)
    objects= ProfesorManager()


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
        ordering = ['numero']
    def __str__(self):
        return self.nombre +'('+self.id_curso + ')'
    id_curso =models.CharField('ID_Curso',max_length=20,unique=True,primary_key=True)
    cod_fecha=models.ForeignKey(Fecha,on_delete=models.CASCADE, related_name='curso')   
    nombre = models.CharField('Nombre', max_length=50)
    electivo=models.CharField('Electivos',max_length=5,choices=electivos_choices, blank=True, null=True)
    numero = models.FloatField('Numero')
    objects = CursoManager()

    id_prof_jefe=models.ForeignKey(Profesor,on_delete=models.CASCADE, related_name='cursos' ,null=True,blank=True)
    plan_estudio=models.ForeignKey(PlanEstudio,on_delete=models.CASCADE,related_name='cursos')
    alumnos = models.ManyToManyField(Alumno,through='Curso_Alumno', related_name='cursos')
    asignaturas = models.ManyToManyField(Asignatura, through='Asignatura_Curso')
# from applications.alumnos.models import Alumno
# alumno = Alumno.objects.get(rut = '16671047-2')
# for p in alumno.parciales.all():
class Asignatura_Curso(models.Model):
    
    class Meta:
        db_table= 'Asignatura_Curso'
        unique_together = (('curso', 'asignatura'),)
    def __str__(self):
        # return self.asignatura.nombre
        return  str(self.curso.numero) + '..' + self.asignatura.nombre + ' -- '+ str(self.curso.cod_fecha.year) + ' ' + str(self.curso.cod_fecha.semestres)
    #Clave primaria de m2m
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)

    #foranea hacia profesores
    id_profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE,related_name='profesor', null=True, blank=True)

class Parciales(models.Model):
    
    fecha = models.DateField('Fecha del parcial')
    calificacion = models.FloatField()
    alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE,related_name='parciales')
    asignatura=models.ForeignKey(Asignatura_Curso,on_delete=models.CASCADE,related_name='parciales')
    

    class Meta:
        verbose_name = 'Parcial'
        verbose_name_plural = 'Parciales'
        db_table= 'Paraciales'
        ordering = ['-id']
    def __str__(self):
        # return self.asignatura.asignatura.nombre 
        return str(self.id)+' -  ' +str(self.calificacion)+ '( ' + str(self.asignatura.asignatura.nombre) + ')'

class Curso_Alumno(models.Model):

    class Meta:
        db_table= 'Curso_Alumno'
        unique_together = (('curso', 'alumno'),)
        ordering=['-id']
    def __str__(self):
        return self.alumno.nombre + ' '+ self.curso.id_curso
    #Clave primaria de m2m
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE)

    #atributo si es curso actual
    is_current = models.BooleanField(default=False)
    abandono =models.BooleanField(default=False)


