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
from applications.alumnos.models import Alumno, Apoderado
from applications.cursos.models import Profesor

class LoginPage(FormView):
    model = User
    template_name = "home/login.html"
    form_class= LoginForm
    success_url=reverse_lazy('home_app:home')

    def form_valid(self, form) :
        path=self.request.get_full_path()
        path = path.split("=",1)
        rut = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(rut=rut,password=password)
        login(self.request,user)

        if len(path) !=2:
            return super(LoginPage,self).form_valid(form)
        else:
            return HttpResponseRedirect(path[1])



class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        print('Sesión expirada')
        return HttpResponseRedirect(reverse('home_app:login'))


class HomePage(LoginRequiredMixin,TemplateView):
    template_name = "home/home.html"
    login_url = reverse_lazy('home_app:login')
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['regulares'] = Alumno.objects.filter(estado = '0').count()
        context['graduados'] = Alumno.objects.filter(estado = '2').count()
        context['desertores'] = Alumno.objects.filter(estado = '1').count()
        context['total'] = Alumno.objects.all().count()
        context['profesores'] = Profesor.objects.all().count()
        context['apoderados'] = Apoderado.objects.all().count()
        context['usuarios'] = User.objects.all().count()
        return context


        
           
