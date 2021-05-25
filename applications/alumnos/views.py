from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView , ListView
from django.views.generic.edit import FormView
# Create your views here.
from applications.alumnos.models import Alumno
from django.contrib.auth.mixins import LoginRequiredMixin
#local
from .forms import AlumnosRegisterForm
class AlumnosHome(LoginRequiredMixin,TemplateView):
    template_name = 'alumnos/inicio.html'
    login_url = reverse_lazy('home_app:login')
class AlumnosFiltros(LoginRequiredMixin,ListView):
    template_name = 'alumnos/filtros.html'
    model = Alumno
    context_object_name = 'alumnos'
    paginate_by=5
    login_url = reverse_lazy('home_app:login')

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        return Alumno.objects.buscar_alumno(palabra_clave)




class AlumnosRegister(LoginRequiredMixin,FormView):
    model = Alumno
    template_name = "alumnos/registrar.html"
    form_class= AlumnosRegisterForm
    success_url='.'
    login_url = reverse_lazy('home_app:login')
    
    def form_valid(self, form):
        Alumno.objects.create(
            rut=form.cleaned_data['rut'],
            nombre=form.cleaned_data['nombre'],
            apellido_paterno=form.cleaned_data['apellido_paterno'],
            apellido_materno=form.cleaned_data['apellido_materno'],
            fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
            rut_apoderado=form.cleaned_data['rut_apoderado'],
            sexo=form.cleaned_data['sexo'],
            telefono=form.cleaned_data['telefono'],
            direccion=form.cleaned_data['direccion'],
            estado=form.cleaned_data['estado'],

        )
        return super(AlumnosRegister, self).form_valid(form)