from django import forms
from applications.errors import DivErrorList
from .models import Alumno
from applications.logicas import validar_rut

class AlumnosRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(AlumnosRegisterForm, self).__init__(*args, **kwargs_new)


    class Meta:
        model=Alumno
        fields= ('__all__')
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold',
                    'placeholder': 'Sin puntos y con guión'
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
                }
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

    # def clean_password2(self):
    #     if self.cleaned_data['password1'] !=self.cleaned_data['password2']:
    #         self.add_error('password2', 'Las contraseñas deben coincidir')
    #         self.fields['password2'].widget.attrs.update({'class': 'form-control rounded-pill my-2 is-invalid'})


    def clean_rut(self):
        if not validar_rut(self.cleaned_data.get("rut")):
            self.add_error('rut', ' *Rut no valido*')
            self.fields['rut'].widget.attrs.update({'class': 'form-control rounded-pill my-2 is-invalid'})
        return self.cleaned_data.get("rut")

 
    