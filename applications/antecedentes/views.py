from django.contrib import messages
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



def antecedente_create(request):
    if request.method == 'POST':

        Antecedente.objects.create(
            nombre_antecedente=request.POST['nombre'],
        )
        messages.success(request,'!!Antecedente añadido con exito!!')
    return HttpResponseRedirect(reverse('antecedentes_app:inicio'))