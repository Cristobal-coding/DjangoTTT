from applications.cursos import models
from django.urls import reverse_lazy, reverse
from django.views.generic import  FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Asignatura
from .forms import AsignaturaForm, PlanesForm
from applications.cursos.models import PlanEstudio, Profesor
from django.contrib import messages
from django.http import HttpResponseRedirect
from applications.cursos.models import Curso
# Create your views here.
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
        print(request.POST)
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
                    asign.id_profesor =Profesor.objects.get(id=key_prof)
                    asign.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])