from django.http.response import HttpResponse
from applications.psicologos.utils import render_to_pdf
from typing import List
from applications.psicologos.forms import InformeForm
from applications.alumnos.models import Alumno
from applications import alumnos
from applications.cursos.models import  Curso_Alumno

from applications.psicologos.models import Informe, Psicologo
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import  FormView

# Create your views here.


class InformeView(LoginRequiredMixin,ListView):
    template_name = "psicologos/inicio.html"
    model = Informe
    context_object_name = 'informe'
    paginate_by=10
    login_url = reverse_lazy('home_app:login')   
    def get_queryset(self):
        rut=self.request.GET.get("rut",'')
        f1=self.request.GET.get("fecha1",'')
        f2=self.request.GET.get("fecha2",'')
        print(rut)
        if f1 and f2:
            if rut:
                return Informe.objects.buscar_informe_fecha_rut(rut,f1,f2)
            else:
                return Informe.objects.buscar_informe_fecha(f1,f2)
        else:
            return Informe.objects.buscar_informe_rut(rut)


class CreateInformeView(LoginRequiredMixin,FormView):
    template_name = "psicologos/addinforme.html"
    model = Informe
    form_class=InformeForm
    login_url = reverse_lazy('home_app:login') 

    def get_context_data(self, **kwargs):
        context = super(CreateInformeView, self).get_context_data(**kwargs)
        context['psicologos'] = Psicologo.objects.all()
        return context
    def form_valid(self, form):
        #El psicologo no viene del form, lo saco del request
        sicologo = Psicologo.objects.get(rut=self.request.POST['sicologo'])
        
        #Aqui crea el informe ....
            #....

        #PD: recuerda en el form.py, eliminar el atributo psicologo, ya que lo creamos a mano
        self.object = form.save() # Esto comentalo
        messages.success(request,'!!Informe creado con exito!!.')
        return super().form_valid(form)
    
class InformeDetailView(DetailView):
    model= Informe
    template_name= "psicologos/informe.html"
    context_object_name='informes'
    def get_context_data(self, **kwargs):
        context = super(InformeDetailView, self).get_context_data(**kwargs)
        # context['curso_alumno'] = Curso_Alumno.objects.all()
        return context

class InformePDFView(View):

    def get(self,request,*args,**kwargs):
        informes = Informe.objects.all()
        data={
            'informe' :informes
        }
        pdf = render_to_pdf("psicologos/informe.html",data)
        return HttpResponse(pdf, content_type='application/pdf')
        


def create(request):
    if request.method == 'POST':
        rut_alumno = Alumno.objects.get(rut = request.POST['rut_alumno'])
        psicologo = Psicologo.objects.get(rut = request.POST['rut_psicologo'])
        Informe.objects.create(
            fecha_emision = request.POST['fecha_emision'],
            pruebas_aplicadas = request.POST['pruebas_aplicadas'],
            motivo = request.POST['motivo'],
            comentario=request.POST['comentario'],
            rut_psicologo=psicologo,
            rut_alumno=rut_alumno,          
        )
    return HttpResponseRedirect(reverse('psicologos_app:inicio'))