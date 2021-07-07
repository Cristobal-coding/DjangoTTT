from django.urls.base import reverse_lazy
from applications.antecedentes.models import Antecedente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
class AntecedentesView(LoginRequiredMixin,ListView):
    template_name = "antecedentes/inicio.html"
    model = Antecedente
    context_object_name = 'antecedentes'
    login_url = reverse_lazy('home_app:login')   