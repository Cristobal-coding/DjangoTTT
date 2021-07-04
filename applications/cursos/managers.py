from django.db import models
from django.db.models import Q , Max


class CursoManager(models.Manager):

    def get_current_cursos(self):
        total = self.all()
        current_año = total.aggregate(Max('cod_fecha__year'))['cod_fecha__year__max']
        current_semestre = total.filter(
            cod_fecha__year = current_año
        ).aggregate(Max('cod_fecha__semestres'))['cod_fecha__semestres__max']
        current_cursos = total.filter(
            Q(cod_fecha__year =current_año ) & Q(cod_fecha__semestres =current_semestre )
        )
        return current_cursos
        
    def get_all_data(self):
        total = self.all()
        current_año = total.aggregate(Max('cod_fecha__year'))['cod_fecha__year__max']
        current_semestre = total.filter(
            cod_fecha__year = current_año
        ).aggregate(Max('cod_fecha__semestres'))['cod_fecha__semestres__max']
        current_cursos = total.filter(
            Q(cod_fecha__year =current_año ) & Q(cod_fecha__semestres =current_semestre )
        )
        return current_cursos, current_año, current_semestre

    