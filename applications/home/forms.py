from django import forms
from applications.logicas import validar_rut
from applications.users.models import User
from applications.errors import DivErrorList
from django.contrib.auth import authenticate
from django.contrib import messages

class LoginPathern(forms.Form):
    username = forms.CharField(
        label='Rut:',
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class': 'form-control border-0 bg-light w-100',
                    'id': 'username',
                    'placeholder': 'Sin puntos y con guión',
                    'style': 'width:100%;'
                    
                }
            ),
    )
    password = forms.CharField(
        label='Contraseña:',
        required=True,
        widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control form-control-sm text-primary bg-light border-0 w-100',
                    'id': 'password',
                    'style': 'width:100%;',
                    'placeholder': 'password'
                }
            ),
    )
    def get_user(self):
        return authenticate(
            rut=self.cleaned_data.get('username', ''),
            password=self.cleaned_data.get('password', ''),
    ) 
    def clean(self):
        if  validar_rut(self.cleaned_data.get("username")):
            user = self.get_user()
            if not user:
                # messages.add_message(self.request, messages.INFO, 'Credenciales Incorrectas.')
                raise forms.ValidationError('Credenciales Incorrectas.')
        else:
            raise forms.ValidationError('Rut no valido')
        return self.cleaned_data
        
    def clean_rut(self):
        if not validar_rut(self.cleaned_data.get("username")):
            self.add_error('rut', 'Rut no valido')      
        return self.cleaned_data.get("username")

class LoginForm(LoginPathern): 
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(LoginForm, self).__init__(*args, **kwargs_new)
  
class LoginAdmin(LoginPathern):   

    def __init__(self, request, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(LoginAdmin, self).__init__(*args, **kwargs_new)

   

