from django import forms
from django.forms import fields, widgets
from applications.errors import DivErrorList
from .models import User, Rol
from applications.validators import validar_rut


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
                    'class': 'form-control my-2',
                    'placeholder': 'Sin puntos y con guión'
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
            self.fields['password2'].widget.attrs.update({'class': 'form-control my-2 is-invalid'})

    def clean_rut(self):
        if not validar_rut(self.cleaned_data.get("rut")):
            self.add_error('rut', 'Rut no valido')
            self.fields['rut'].widget.attrs.update({'class': 'form-control my-2 is-invalid'})
        return self.cleaned_data.get("rut")

class RolRegisterForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(RolRegisterForm, self).__init__(*args, **kwargs_new)


    class Meta:
        model=Rol
        fields= ('nombre',)
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control my-2',
                }
            ),
  
        }
    def clean_nombre(self):
        name =self.cleaned_data.get("nombre")
        existe = Rol.objects.filter(nombre__iexact=name).exists()
        if existe: 
            # self.add_error('nombre', 'Formato de nombre invalido')    
            raise forms.ValidationError('Este nombre ya esta Ingresado.')
        return self.cleaned_data.get("nombre")
    # def clean_nombre(self):
    #     if self.cleaned_data.get("rut").unique:
    #         self.add_error('rut', 'Rut no valido')
    #         self.fields['rut'].widget.attrs.update({'class': 'form-control my-2 is-invalid'})
    #     return self.cleaned_data.get("rut")
 
    