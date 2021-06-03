from django import forms
from applications.logicas import validar_rut
from applications.users.models import User
from applications.errors import DivErrorList
from django.contrib.auth import authenticate, login
from django.contrib import messages

class LoginForm(forms.Form):
    rut = forms.CharField(
        label='Rut:',
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class': 'form-control border-0 bg-light',
                    'id': 'rut',
                    'placeholder': 'rut'
                    
                }
            ),
    )
    password = forms.CharField(
        label='Contraseña:',
        required=True,
        widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control form-control-sm text-primary bg-light border-0',
                    'id': 'password',
                    'placeholder': 'password'
                }
            ),
    )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        rut = self.cleaned_data.get("rut")
        password=self.cleaned_data.get("password")
        print(self.cleaned_data.get("username"))
        user = authenticate(rut=rut,password=password)
        if not user:
            # messages.add_message(self.request, messages.INFO, 'Credenciales Incorrectas.')
            raise forms.ValidationError('Credenciales Incorrectas.')
        else:
            if not user.activo:
                # messages.add_message(self.request, messages.INFO, 'Usuario Bloqueado.')
                raise forms.ValidationError('Usuario Bloqueado.')
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(LoginForm, self).__init__(*args, **kwargs_new)

    def clean_rut(self):
        if not validar_rut(self.cleaned_data.get("rut")):
            self.add_error('rut', 'Rut no valido')      
        return self.cleaned_data.get("rut")

class LoginAdmin(forms.Form):
    def clean(self):
        cleaned_data = super(LoginAdmin, self).clean()
        rut = self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user = authenticate(rut=rut,password=password)
        if not user:
            raise forms.ValidationError('')
        else:
            if not user.activo:
                raise forms.ValidationError('')
        return self.cleaned_data