from django.contrib import admin
# from django.contrib.admin.widgets import multip

# Register your models here.
from .models import Fecha, Profesor, Curso,Curso_Alumno,Asignatura_Curso
# Register your models here.
admin.site.register(Fecha)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Curso_Alumno)
admin.site.register(Asignatura_Curso)
