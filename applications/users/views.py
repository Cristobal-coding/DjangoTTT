from applications.cursos.models import Profesor
from applications.psicologos.models import Psicologo
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from .models import User, Rol
from .forms import RolRegisterForm, UserRegisterForm
from datetime import date, datetime
import psycopg2


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "usuarios/profile.html"
    login_url = reverse_lazy('home_app:login')

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
   
class CreateUser(LoginRequiredMixin,CreateView):
    form_class= UserRegisterForm
    success_url = '.'
    login_url = reverse_lazy('home_app:login')
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
        print(form.cleaned_data['rol'])
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['rut'],
            form.cleaned_data['password1'],
            rol=form.cleaned_data['rol'],        
        ) 
        if str(form.cleaned_data['rol']).strip() == 'Psicologo':
            Psicologo.objects.create(
            rut= form.cleaned_data['rut'],
            nombre=form.cleaned_data['username'],
            apellido_paterno="",
            apellido_materno="",
            correo=None,
            telefono="",
            fecha_ingreso=date.today()
            )
        elif str(form.cleaned_data['rol']).strip() == 'Profesor':
            Profesor.objects.create(
            rut=form.cleaned_data['rut'],
            nombres=form.cleaned_data['username'],
            apellido_paterno="",
            apellido_materno="",
            asig_impartir=None,
            )
            
        return HttpResponseRedirect(reverse('user_app:registrar'),)
        
class CreateRol(LoginRequiredMixin,CreateView):
    form_class= RolRegisterForm
    success_url = '.'
    login_url = reverse_lazy('home_app:login')
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
        print('========')
        print(form)
        print('========')
        return self.render_to_response(self.get_context_data(rolform=form))

    def form_valid(self, form):
        Rol.objects.create(nombre=form.cleaned_data['nombre'])
        return HttpResponseRedirect(reverse('user_app:registrar'),)

class EditRol(LoginRequiredMixin,UpdateView):
    form_class = RolRegisterForm
    model = Rol
    success_url = reverse_lazy('user_app:registrar')
    login_url = reverse_lazy('home_app:login')
    def form_invalid(self, form):
        self.object = self.get_object()
        rol_id=self.object.id
        formulario=str(form)
        if 'nombre invalido' in formulario:
            print('ERROES TITLE')

            messages.error(self.request,str(rol_id)+'*')
        else:
            print('ERROR UNIQUE')

            messages.error(self.request,rol_id)
        return HttpResponseRedirect(reverse('user_app:registrar'),)
    def form_valid(self, form):
        messages.success(self.request,'Rol actualizado Correctamente.')
        return HttpResponseRedirect(self.get_success_url())
    login_url = reverse_lazy('home_app:login')


def DeleteRol(request, pk):
    query = Rol.objects.get(pk=pk)
    query.delete()
    messages.add_message(request, messages.INFO, 'Rol elminado Satisfactoriamente.')
    return HttpResponseRedirect(reverse('user_app:registrar'))
    # def get_template_names(self):
    #     return 'user_app:registrar'
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