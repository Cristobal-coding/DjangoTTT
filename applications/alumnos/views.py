from django.shortcuts import render
from django.views.generic import TemplateView , ListView
# Create your views here.
from applications.alumnos.models import Alumno

class AlumnosHome(TemplateView):
    template_name = 'alumnos/inicio.html'

class AlumnosFiltros(ListView):
    template_name = 'alumnos/filtros.html'
    model = Alumno
    context_object_name = 'alumnos'