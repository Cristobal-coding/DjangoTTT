from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView , ListView, UpdateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import  FormView
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.alumnos.models import Alumno, Apoderado
#local
from .forms import AlumnosRegisterForm, ApoderadosRegisterForm

class AlumnosHome(LoginRequiredMixin,TemplateView):
    template_name = 'alumnos/inicio.html'
    login_url = reverse_lazy('home_app:login')
    
    def get_context_data(self, **kwargs):
        context = super(AlumnosHome, self).get_context_data(**kwargs)
        context['alumnos'] = Alumno.objects.count()
        context['apoderados'] = Apoderado.objects.count()
        context['fem'] = Alumno.objects.filter(sexo__icontains='0')
        context['masc'] = Alumno.objects.filter(sexo__icontains='1')
        return context

class AlumnosFiltros(LoginRequiredMixin,ListView):
    template_name = 'alumnos/filtros.html'
    model = Alumno
    context_object_name = 'alumnos'
    paginate_by=5
    login_url = reverse_lazy('home_app:login')
    

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        f1=self.request.GET.get("fecha1",'')
        f2=self.request.GET.get("fecha2",'')
        sexo=self.request.GET.get("sexo",'')
        if sexo:
            if f1 and f2 and palabra_clave:
                return Alumno.objects.buscar_alumno_fecha_s(palabra_clave,f1,f2,sexo)
            elif palabra_clave and f1==""and f2=="":
                return Alumno.objects.buscar_alumno_s(palabra_clave,sexo)
            else:
                return Alumno.objects.buscar_por_sexo(sexo)
        else:
            if f1 and f2:
                return Alumno.objects.buscar_alumno_fecha(palabra_clave,f1,f2)
            else:
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

class AlumnoEdit(LoginRequiredMixin,UpdateView):
    template_name = "alumnos/edit.html"
    form_class = AlumnosRegisterForm
    model = Alumno
    success_url = reverse_lazy('alumnos_app:filtrar')
    login_url = reverse_lazy('home_app:login')
    
class ApoderadosList(LoginRequiredMixin,ListView):
    template_name= 'alumnos/apoderados.html'
    model=Apoderado
    context_object_name='apoderados'
    paginate_by=5
    login_url = reverse_lazy('home_app:login')

class CreateApoderado(LoginRequiredMixin, FormView):
    model = Apoderado
    template_name = "alumnos/regist_apod.html"
    form_class= ApoderadosRegisterForm
    success_url='.'
    login_url = reverse_lazy('home_app:login')
    def form_valid(self, form):
        Apoderado.objects.create(
            rut=form.cleaned_data['rut'],
            nombre_apoderado=form.cleaned_data['nombre_apoderado'],
            apellido_paterno=form.cleaned_data['apellido_paterno'],
            apellido_materno=form.cleaned_data['apellido_materno'],
            telefono_apoderado=form.cleaned_data['telefono_apoderado'],
            correo=form.cleaned_data['correo'],
        )
        messages.add_message(self.request, messages.INFO, 'Apoderado ingresado Correctamente.')
        return HttpResponseRedirect(self.get_success_url())
    
def delete_alumno(request, pk):
    query = Alumno.objects.get(pk=pk)
    query.delete()
    return HttpResponseRedirect(reverse('alumnos_app:filtrar'))
