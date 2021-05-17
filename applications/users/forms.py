from django import forms
from django.forms import fields, widgets
from applications.errors import DivErrorList
from .models import User
from applications.logicas import validar_rut
class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control my-2',
                    
                }
            ),
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        required=True,
        widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control my-2',
                    'placeholder': 'Confirmar Contraseña'
                }
            ),
    )
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(UserRegisterForm, self).__init__(*args, **kwargs_new)

    class Meta:
        model=User
        fields= ('username','rut','rol')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control my-2'
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control my-2'
                }
            ),
            'rol': forms.Select(
                attrs={
                    'class': 'form-select my-2'
                }
            ),
           
            
        }

    def clean_password2(self):
        if self.cleaned_data['password1'] !=self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas deben coincidir')

    def clean_rut(self):
        if not validar_rut(self.cleaned_data.get("rut")):
            self.add_error('rut', 'Rut no valido')
        return self.cleaned_data.get("rut")

 
    