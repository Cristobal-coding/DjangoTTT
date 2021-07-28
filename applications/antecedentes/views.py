from applications.alumnos.models import Alumno_antecedente
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse, reverse_lazy
from applications.antecedentes.models import Antecedente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
class AntecedentesView(LoginRequiredMixin,ListView):
    template_name = "antecedentes/antecedentes.html"
    model = Antecedente
    context_object_name = 'antecedentes'
    login_url = reverse_lazy('home_app:login')   
    paginate_by=11
    def get_context_data(self, **kwargs):
        context = super(AntecedentesView, self).get_context_data(**kwargs)
        context['alumno_antecedente'] = Alumno_antecedente.objects.all()[:20]
        return context

def antecedente_create(request):
    if request.method == 'POST':
        nombreAdd=request.POST['nombre']
        if Antecedente.objects.filter(nombre_antecedente__iexact=nombreAdd):            
             messages.error(request,'Ya existe ese nombre')
        elif nombreAdd=="":
            messages.error(request,'Ingrese un antecedente.') 
        else:
            Antecedente.objects.create(
                nombre_antecedente=(request.POST['nombre']).lower(),
            )
            messages.success(request,'!!Antecedente añadido con exito!!')
       
        # print("request: ", request.POST)
        
    return HttpResponseRedirect(reverse('antecedentes_app:inicio'))
   


def edit_antecedente(request,pk):
    if request.method == 'POST':
        nombreAdd=request.POST['nombre']
        if Antecedente.objects.filter(nombre_antecedente__iexact=nombreAdd):            
            messages.error(request,'Ya existe ese nombre')
        elif nombreAdd=="":
            messages.error(request,'Ingrese un antecedente.') 
        else:
            query=Antecedente.objects.get(pk=pk)
            query.nombre_antecedente = request.POST['nombre']
            query.save()
    return HttpResponseRedirect(reverse('antecedentes_app:inicio'))