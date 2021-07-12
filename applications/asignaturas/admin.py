from django.contrib import admin

from .models import Asignatura, PlanEstudio, Parciales
# Register your models here.
admin.site.register(Asignatura)
admin.site.register(PlanEstudio)
admin.site.register(Parciales)