from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import UserRegisterForm

class UserMainView(LoginRequiredMixin,FormView):
    model = User
    template_name = "usuarios/inicio.html"
    form_class= UserRegisterForm
    success_url='.'
    login_url = reverse_lazy('home_app:login')

    def get_context_data(self, **kwargs):
        context = super(UserMainView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['rut'],
            form.cleaned_data['password1'],
            rol=form.cleaned_data['rol'],

        )
        return super(UserMainView, self).form_valid(form)

def unlock(request, pk):
    query = User.objects.get(pk=pk)
    if(request.user.rut != query.rut):
        query.activo=True
        query.save()
    else:
        messages.add_message(request, messages.INFO, 'No puedes Aplicar estas acciones sobre ti Mismo.')
    # query.delete()
    return HttpResponseRedirect(reverse('user_app:registrar'))

def lock(request, pk):
    query = User.objects.get(pk=pk)
    if(request.user.rut != query.rut):
        query.activo=False
        query.save()
    else:
        messages.add_message(request, messages.INFO, 'No puedes Aplicar estas acciones sobre ti Mismo.')
    # query.delete()
    return HttpResponseRedirect(reverse('user_app:registrar'))