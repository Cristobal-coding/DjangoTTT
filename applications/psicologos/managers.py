import datetime
from django.db import models
from django.db.models import Q

class InformeManager(models.Manager):
    def buscar_informe_fecha_rut(self, rut,f1,f2):
        f1=datetime.datetime.strptime(f1,"%Y-%m-%d").date()
        f2=datetime.datetime.strptime(f2,"%Y-%m-%d").date()
        resultado =self.filter(
            Q(rut_alumno__rut__icontains=rut),
            fecha_emision__range=(f1,f2) 
            ).order_by('-fecha_emision')
        return resultado

    def buscar_informe_fecha(self,f1,f2):
        resultado =self.filter(
            fecha_emision__range=(f1,f2) 
            ).order_by('-fecha_emision')
        return resultado

    def buscar_informe_rut(self, rut):
        
        resultado =self.filter(
            Q(rut_alumno__rut__icontains=rut),         
            ).order_by('-fecha_emision')
        return resultado