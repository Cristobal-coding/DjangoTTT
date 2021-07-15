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
    def get_cursos_by_id(self, id, año, semestre):
        total = self.all()
        current_cursos = total.filter(
            Q(cod_fecha__year =año ) & Q(cod_fecha__semestres =semestre )
        )
        filtro = current_cursos.filter(
            id_curso__icontains=id
        )
        return filtro

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
    def get_año_semestre(self):
        total = self.all()
        current_año = total.aggregate(Max('cod_fecha__year'))['cod_fecha__year__max']
        current_semestre = total.filter(
            cod_fecha__year = current_año
        ).aggregate(Max('cod_fecha__semestres'))['cod_fecha__semestres__max']
       
        return current_año, current_semestre
    
    def get_curso_with_fecha(self, year, semestre, rut):
        cursos =  self.filter(
            Q(cod_fecha__year =year ) & Q(cod_fecha__semestres =semestre )
        )

        for c in cursos:
            for alumno in c.alumnos.all():
                if alumno.rut == rut:
                    curso = c
        return curso

    # def prove_Asign(self):
    #     result= self.all()
    #     for i in result:
    #         print(i.asignatura_curso_set.all())
            # from applications.cursos.models import Curso
            # asign = Curso.objects.prove_Asign()

   
    