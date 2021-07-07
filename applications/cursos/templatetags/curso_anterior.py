from applications.cursos.logicas import curso_anterior
from django import template
register = template.Library()

@register.simple_tag

def get_anterior_curso(numero):
    curso = curso_anterior(numero=numero)
    return curso
    