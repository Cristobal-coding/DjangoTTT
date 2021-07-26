from django.db import models
from django.db.models import Q , Max

class FechaManager(models.Manager):
    def get_years(self):
        years = []
        for fecha in self.all():
            if not fecha.year in years:
                years.append(fecha.year)
        return years

class ProfesorManager(models.Manager):
    def get_jefes(self):
        profesores = []
        for profe in self.all():
            if profe.cursos.count() > 0:
                profesores.append(profe)
        return profesores

class CursoManager(models.Manager):

    def get_cursos_filter(self, values):
        cursos = self.all()
        if values[0] != '':
            if values[1] != '' and values[2] != '':
                result = cursos.filter(
                    Q( id_curso__icontains = values[0]) &
                    Q(cod_fecha__year = values[1]) &
                    Q(cod_fecha__semestres = values[2]) 
                )
            elif values[1] != '' and values[2] == '':
                result = cursos.filter(
                    Q( id_curso__icontains = values[0]) &
                    Q(cod_fecha__year = values[1])
                )
            elif values[1] == '' and values[2] != '':
                result = cursos.filter(
                    Q( id_curso__icontains = values[0]) &
                    Q(cod_fecha__semestres = values[2]) 
                )
            else:
                result = cursos.filter(
                    id_curso__icontains = values[0]
                )
            #end
        elif values[3] != '':
            result = cursos.filter(
                Q(id_prof_jefe__id = values[3]) 
            )
        elif values[1] != '' and values[2] != '':
            result = cursos.filter(
                Q(cod_fecha__year = values[1]) &
                Q(cod_fecha__semestres = values[2]) 
            )
        elif values[1] != '' and values[2] == '':
            result = cursos.filter(
                Q(cod_fecha__year = values[1])
            )
        elif values[1] == '' and values[2] != '':
            result = cursos.filter(
                Q(cod_fecha__semestres = values[2]) 
            )
        else:
            result = self.all()
        return result
        # return self.all()

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

    def alumnos_cuarto(self, year, semestre):
        total= self.all()
        cuartos = total.filter(
            Q(numero__in = [12.0,12.1,12.2]) &
            Q(cod_fecha__year = year) &
            Q(cod_fecha__semestres = semestre)
        )
        alumnos=[]
        for curso in cuartos:
            for alumno in curso.alumnos.all():
                alumnos.append(alumno)
        return alumnos
    # from applications.cursos.models import Curso
#    curso = Curso.objects.alumnos_cuarto(2021,'1')
    