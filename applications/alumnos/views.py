from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView , ListView
# Create your views here.
from applications.alumnos.models import Alumno
from django.contrib.auth.mixins import LoginRequiredMixin
class AlumnosHome(LoginRequiredMixin,TemplateView):
    template_name = 'alumnos/inicio.html'
    login_url = reverse_lazy('home_app:login')
class AlumnosFiltros(LoginRequiredMixin,ListView):
    template_name = 'alumnos/filtros.html'
    model = Alumno
    context_object_name = 'alumnos'
    paginate_by=4
    login_url = reverse_lazy('home_app:login')
    
    