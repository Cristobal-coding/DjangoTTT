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
    login_url = reverse_lazy('home_app:login')
    paginate_by=8
    model=Informe
    context_object_name="informe"