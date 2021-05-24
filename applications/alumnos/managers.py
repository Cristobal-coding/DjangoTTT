from django.db import models

class AlumnoManager(models.Manager):
    def buscar_alumno(self, kword):
        resultado =self.filter(
            nombre__icontains=kword
            )
        return resultado