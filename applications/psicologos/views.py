from applications.psicologos.models import Informe, Psicologo
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
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
          
            
   