from applications.alumnos.models import Alumno
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
# Create your views here.
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, View
from applications.users.models import User
from .forms import LoginForm
from django.contrib import messages
class LoginPage(FormView):
    model = User
    template_name = "home/login.html"
    form_class= LoginForm
    success_url=reverse_lazy('home_app:home')

    def form_valid(self, form) :
        username = self.request.POST['rut']
        password = self.request.POST['password']
        user = authenticate(username=username,password=password)
        if user.activo:
            login(self.request,user)
            return redirect(reverse('home_app:home'))
        else:
            messages.add_message(self.request, messages.INFO, 'Usuario Bloqueado.')
            return redirect(reverse('home_app:login'))
        # return super(LoginPage,self).form_valid(form)

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('home_app:login'))


class HomePage(LoginRequiredMixin,TemplateView):
    template_name = "home/home.html"
    login_url = reverse_lazy('home_app:login')

    # def get_context_data(self, **kwargs):
    #     context = super(HomePage, self).get_context_data(**kwargs)
    #     context['alumnos'] = Alumno.objects.buscar_alumno('f')
    #     return context


        
           
