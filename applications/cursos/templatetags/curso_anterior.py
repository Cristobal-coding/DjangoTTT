from applications.cursos.logicas import curso_anterior
from django import template
from applications.cursos.models import Curso
register = template.Library()

@register.simple_tag

def get_anterior_curso(numero):
    curso = curso_anterior(numero=numero)
    return curso
    
@register.simple_tag
def get_curso_pasado(alumno):
    unused , año , semestre= Curso.objects.get_all_data()
    founded = False
    cursos = alumno.curso_alumno_set.all()
    if len(cursos) > 0 :
        for c in cursos:
            if c.curso.cod_fecha.year == año-1:
                founded = True
                nombre=c.curso.nombre
    if founded :
        return nombre
    else:
        return 'Sin Curso'

@register.simple_tag
def get_all_pks(alumnos, rut):
    ruts = []
    for i in alumnos:
        ruts.append(i.alumno.rut)
    return rut in ruts
    