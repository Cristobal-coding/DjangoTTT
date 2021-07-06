from applications.antecedentes.models import Antecedente, Antecedente_tipo, Tipo
from django.contrib import admin

# Register your models here.
admin.site.register(Antecedente)
admin.site.register(Tipo)
admin.site.register(Antecedente_tipo)