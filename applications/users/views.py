from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from .models import User
from .forms import UserRegisterForm
class UserRegisterView(FormView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class= UserRegisterForm
    success_url='.'
    
    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['rut'],
            form.cleaned_data['password1'],
            rol=form.cleaned_data['rol'],

        )
        return super(UserRegisterView, self).form_valid(form)