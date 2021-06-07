from django import forms
from applications.errors import DivErrorList
from .models import Alumno, Apoderado
from applications.logicas import validar_rut

class AlumnosPathern(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(AlumnosPathern, self).__init__(*args, **kwargs_new)

    def clean_rut(self):
        if not validar_rut(self.cleaned_data.get("rut")):
            self.add_error('rut', ' *Rut no valido*')
            self.fields['rut'].widget.attrs.update({'class': 'form-control rounded-pill my-2 is-invalid'})
        return self.cleaned_data.get("rut")

class AlumnosRegisterForm(AlumnosPathern):

    class Meta:
        model=Alumno
        fields= ('__all__')
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold',
                    'placeholder': 'Sin puntos y con guión'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold',          
                }
            ),
            'apellido_paterno': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold'
                }
            ),   
            'apellido_materno': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold'
                }
            ),   
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control rounded-pill my-2',
                    'type': 'date'
                },
                format='%Y-%m-%d'
            ),   
            'rut_apoderado': forms.Select(
                attrs={
                    'class': 'form-select rounded-pill my-2'
                }
            ),   
            'sexo': forms.Select(
                attrs={
                    'class': 'form-select rounded-pill my-2'
                }
            ),   
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold',
                    'placeholder': '8 digitos'
                }
            ),   
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold'
                }
            ),   
            'estado': forms.Select(
                attrs={
                    'class': 'form-select rounded-pill my-2'
                }
            ),   
        }

class ApoderadosRegisterForm(AlumnosPathern):
    
    class Meta:
        model=Apoderado
        fields= ('__all__')
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold',
                    'placeholder': 'Sin puntos y con guión'
                }
            ),
            'nombre_apoderado': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold'
                }
            ),
            'apellido_paterno': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold'
                }
            ),   
            'apellido_materno': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold'
                }
            ),    
            'telefono_apoderado': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold',
                    'placeholder': '8 digitos'
                }
            ),   
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold',
                    'placeholder': 'apoderado@gmail.com ...',
                    'type':'email'
                }
            ),     
        }
    def clean_telefono_apoderado(self):
        if not self.cleaned_data.get("telefono_apoderado").isdigit():
            self.add_error('telefono_apoderado', ' *Telefono invalido*')
            self.fields['telefono_apoderado'].widget.attrs.update({'class': 'form-control rounded-pill my-2 is-invalid'})
        return self.cleaned_data.get("telefono_apoderado")
    def clean_correo(self):
        correo =self.cleaned_data.get("correo")
        if not 'gmail' in correo and not 'hotmail' in correo :
            self.add_error('correo', ' *Correo invalido*')
            self.fields['correo'].widget.attrs.update({'class': 'form-control rounded-pill my-2 is-invalid'})
        return self.cleaned_data.get("correo")

 
    