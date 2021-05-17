from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
# Create your views here.
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from applications.users.models import User
from .forms import LoginForm

class LoginPage(FormView):
    model = User
    template_name = "home/login.html"
    form_class= LoginForm
    success_url=reverse_lazy('home_app:home')

    def form_valid(self, form) :
        usuario = authenticate(
            rut= form.cleaned_data['rut'],
            password= form.cleaned_data['password'],
        )
        login(self.request, usuario)
        return super(LoginPage,self).form_valid(form)

class HomePage(TemplateView):
    template_name = "home/home.html"
