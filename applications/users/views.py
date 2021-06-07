from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Rol
from .forms import RolRegisterForm, UserRegisterForm

class UserMainView(LoginRequiredMixin,TemplateView):
    template_name = "usuarios/inicio.html"
    login_url = reverse_lazy('home_app:login')

    def get_context_data(self, **kwargs):
        context = super(UserMainView, self).get_context_data(**kwargs)
        context['userform'] = UserRegisterForm
        context['rolform'] = RolRegisterForm
        context['users'] = User.objects.all()
        context['roles'] = Rol.objects.all()
        return context
   
class CreateUser(CreateView):
    form_class= UserRegisterForm
    success_url = '.'

    def render_to_response(self, context, **response_kwargs):
        context['users'] = User.objects.all()
        context['roles'] = Rol.objects.all()
        context['rolform'] = RolRegisterForm
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template='usuarios/inicio.html',
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(userform=form))

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['rut'],
            form.cleaned_data['password1'],
            rol=form.cleaned_data['rol'],
        )
        return HttpResponseRedirect(reverse('user_app:registrar'),)
        
class CreateRol(CreateView):
    form_class= RolRegisterForm
    success_url = '.'

    def render_to_response(self, context, **response_kwargs):
        context['users'] = User.objects.all()
        context['roles'] = Rol.objects.all()
        context['userform'] = UserRegisterForm
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template='usuarios/inicio.html',
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(rolform=form))

    def form_valid(self, form):
        Rol.objects.create(nombre=form.cleaned_data['nombre'])
        return HttpResponseRedirect(reverse('user_app:registrar'),)

# def unlock(request, pk):
#     query = User.objects.get(pk=pk)
#     if(request.user.rut != query.rut):
#         query.activo=True
#         query.save()
#     else:
#         messages.add_message(request, messages.INFO, 'No puedes Aplicar estas acciones sobre ti Mismo.')
#     # query.delete()
#     return HttpResponseRedirect(reverse('user_app:registrar'))

# def lock(request, pk):
#     query = User.objects.get(pk=pk)
#     if(request.user.rut != query.rut):
#         query.activo=False
#         query.save()
#     else:
#         messages.add_message(request, messages.INFO, 'No puedes Aplicar estas acciones sobre ti Mismo.')
#     # query.delete()
#     return HttpResponseRedirect(reverse('user_app:registrar'))