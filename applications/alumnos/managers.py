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


    # def buscar_fecha(self, fecha1,fecha2):

    #     resultado=