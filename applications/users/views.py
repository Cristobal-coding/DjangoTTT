from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import UserRegisterForm

class UserRegisterView(LoginRequiredMixin,FormView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class= UserRegisterForm
    success_url='.'
    login_url = reverse_lazy('home_app:login')
    
    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['rut'],
            form.cleaned_data['password1'],
            rol=form.cleaned_data['rol'],

        )
        return super(UserRegisterView, self).form_valid(form)