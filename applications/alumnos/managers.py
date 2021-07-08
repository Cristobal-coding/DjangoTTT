import datetime
from django.db import models
from django.db.models import Q

class AlumnoManager(models.Manager):
    def buscar_alumno(self, kword):
        resultado =self.filter(
            Q(nombre__icontains=kword) | Q(apellido_paterno__icontains=kword) | Q(apellido_materno__icontains=kword)
            ).order_by('apellido_paterno')
        return resultado
    def buscar_alumno_fecha(self, kword,fecha1,fecha2):
        f1= datetime.datetime.strptime(fecha1,"%Y-%m-%d").date()
        f2= datetime.datetime.strptime(fecha2,"%Y-%m-%d").date()
        resultado =self.filter(
            (Q(nombre__icontains=kword) | Q(apellido_paterno__icontains=kword) | Q(apellido_materno__icontains=kword)),
            fecha_nacimiento__range=(f1,f2)
            ).order_by('apellido_paterno')
        return resultado
    #ORDENADOS POR SEXO
    def buscar_por_sexo(self,sex):
        resultado=self.filter(sexo=sex)
        return resultado
    def buscar_alumno_s(self, kword,sex):
        resultado =self.filter(
            (Q(nombre__icontains=kword) | Q(apellido_paterno__icontains=kword) | Q(apellido_materno__icontains=kword)), sexo=sex
            ).order_by('apellido_paterno')
        return resultado
    def buscar_alumno_fecha_s(self, kword,fecha1,fecha2,sex):
        f1= datetime.datetime.strptime(fecha1,"%Y-%m-%d").date()
        f2= datetime.datetime.strptime(fecha2,"%Y-%m-%d").date()
        resultado =self.filter(
            (Q(nombre__icontains=kword) | Q(apellido_paterno__icontains=kword) | Q(apellido_materno__icontains=kword)),
            fecha_nacimiento__range=(f1,f2), sexo=sex
            ).order_by('apellido_paterno')
        return resultado
    
    # from applications.alumnos.models import Alumno
    # result = Alumno.objects.get_alumno_sin_curso()    
    #Retorna alumnos sin curso, y que ademas tengan estado regular
    def get_alumno_sin_curso(self):
        total = self.all()
        result=[]
        for a in total:
            if a.estado == '0':
                for pivot in a.curso_alumno_set.all():
                    if not pivot.is_current: 
                        result.append(a)
        return result
            
class ApoderadoManager(models.Manager):
    def buscar_apoderado(self, nombre):
        resultado =self.filter(
            Q(nombre_apoderado__icontains=nombre) | Q(apellido_paterno__icontains=nombre) | Q(apellido_materno__icontains=nombre)
            ).order_by('apellido_paterno')
        return resultado
    def buscar_apoderado_rut(self, nombre,rut):
        resultado =self.filter(
            (Q(nombre_apoderado__icontains=nombre) | Q(apellido_paterno__icontains=nombre) | Q(apellido_materno__icontains=nombre)), rut__icontains=rut
            ).order_by('apellido_paterno')
        return resultado
   
    # def buscar_fecha(self, fecha1,fecha2):

    #     resultado=