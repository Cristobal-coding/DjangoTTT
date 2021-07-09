from django.contrib import admin

from .models import Alumno_antecedente, Apoderado, Alumno
# Register your models here.
admin.site.register(Apoderado)
admin.site.register(Alumno)
admin.site.register(Alumno_antecedente)