from django.views.generic.edit import CreateView
from applications.cursos import models
from django.urls import reverse_lazy, reverse
from django.views.generic import  FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Asignatura
from .forms import AsignaturaForm, PlanesForm
from applications.cursos.models import PlanEstudio, Profesor
from django.contrib import messages
from django.http import HttpResponseRedirect
from applications.cursos.models import Curso
from .logics import asignaturas_base, planes_base
# Create your views here.

class ProfesoresView(LoginRequiredMixin, ListView):
    model =Profesor
    template_name= 'asignaturas/profesores.html'
    login_url = reverse_lazy('home_app:login')
    context_object_name = 'profesores'    

    def get_context_data(self, **kwargs):
        context = super(ProfesoresView, self).get_context_data(**kwargs)
        # context['profesores'] = Profesor.objects.all()
        context['asignaturas'] = Asignatura.objects.all()
        return context

class AsignaturasView(LoginRequiredMixin, FormView):
    model =Asignatura
    template_name= 'asignaturas/overview.html'
    form_class= AsignaturaForm
    success_url='.'
    login_url = reverse_lazy('home_app:login')

    def get_context_data(self, **kwargs):
        context = super(AsignaturasView, self).get_context_data(**kwargs)
        context['asignaturas'] = Asignatura.objects.all()
        return context
    def form_valid(self, form):
        nombre = form.cleaned_data['nombre'].capitalize()
        cod = form.cleaned_data['cod_asign'].upper()
        Asignatura.objects.create(
            cod_asign = cod,
            nombre = nombre,
        )
        messages.success(self.request, 'Asignatura registrada con exito.')
        return HttpResponseRedirect(self.get_success_url())

class PlanesView(LoginRequiredMixin, FormView):
    template_name= 'asignaturas/planes.html'
    model =PlanEstudio
    form_class= PlanesForm
    success_url='.'
    login_url = reverse_lazy('home_app:login')

    def get_context_data(self, **kwargs):
        context = super(PlanesView, self).get_context_data(**kwargs)
        context['planes'] = PlanEstudio.objects.all()
        context['profs'] = Profesor.objects.all()
        return context
    def form_valid(self, form):
        nombre = form.cleaned_data['nombre'].capitalize()
        PlanEstudio.objects.create(
            nombre = nombre,
            detalle_url = form.cleaned_data['detalle_url']
        )
        plan = PlanEstudio.objects.filter(
            nombre__iexact = nombre
        )
        asignaturas = form.cleaned_data['asignaturas']
        for pl in plan:
            for a in asignaturas:
                pl.asignaturas.add(a.cod_asign)
                
        messages.success(self.request, 'Asignatura registrada con exito.')
        return HttpResponseRedirect(self.get_success_url())

def profe_to_asign(request,):
    if request.method == 'POST':
        key_asign = request.POST['asignatura']
        key_prof = request.POST['profesor']
        key_curso = request.POST['curso']
        curso = Curso.objects.get(id_curso= key_curso)
 
        for asign in curso.asignatura_curso_set.all():
            if asign.asignatura.cod_asign == key_asign:
                if key_prof == '':
                    asign.id_profesor =None
                    asign.save()
                else:
                    asign.id_profesor =Profesor.objects.get(rut=key_prof)
                    asign.save()
        messages.success(request,'!!Profesor actualizado con exito!!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def init_all(request,):
    if request.method == 'POST':
        # Primer crear los planes de estudio
        for plan in planes_base:
            PlanEstudio.objects.create(
                nombre = plan[0],
                detalle_url = plan[1]
            )
        
        for asign in asignaturas_base:  
            plan = PlanEstudio.objects.get(nombre=asign[2])     
            Asignatura.objects.create(
                cod_asign=asign[0],
                nombre=asign[1],
                plan=plan
            )
        messages.success(request,'!!Planes de estudio y Asignaturas generados con Exito!!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def profesor_create(request):
    if request.method == 'POST':
            if Profesor.objects.filter(rut__iexact=request.POST['rut']).exists():
                messages.error(request,"Ya existe un profesor con ese rut.")
            else:
                Profesor.objects.create(
                    rut=request.POST['rut'],
                    nombres=request.POST['nombre'].capitalize(),
                    apellido_paterno=request.POST['paterno'].capitalize(),
                    apellido_materno=request.POST['materno'].capitalize(),
                    asig_impartir=Asignatura.objects.get(cod_asign=request.POST['asignatura'],)
                )
                messages.success(request,'!!Profesor añadido con exito!!')

    return HttpResponseRedirect(reverse('asignaturas_app:profesores'))
def profesor_edit(request):
    #validar
    if request.method == 'POST':
        profesor = Profesor.objects.get(rut=request.POST['profesor'])
        profesor.nombres=request.POST['nombre']
        profesor.apellido_paterno=request.POST['paterno']
        profesor.apellido_materno=request.POST['materno']
        if request.POST['asignatura']=="":
            profesor.asig_impartir=None
        else:     
            profesor.asig_impartir=Asignatura.objects.get(cod_asign=request.POST['asignatura'],)
        profesor.save()
        messages.success(request,'!!Profesor actualizado con exito!!')
    return HttpResponseRedirect(reverse('asignaturas_app:profesores'))