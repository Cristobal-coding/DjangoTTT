from django import forms
from django.db.models import fields
from applications.errors import DivErrorList
from .models import Alumno, Apoderado, Alumno_antecedente
from applications.cursos.models import Parciales, Curso
from applications.validators import validar_rut
from django.forms import ModelChoiceField, widgets


class Alumno_AntecedenteForm(forms.ModelForm):
    class Meta:
        model=Alumno_antecedente
        fields= ('detalle', 'antecedente', 'fecha')
        widgets={
            'antecedente' : forms.Select(
                attrs={
                    'class' : 'form-select'
                }
            ),
            'fecha' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'type': 'date'
                }
            )
        }

class CertificadoForm(forms.Form):
    coeficientes = [
        ['1', 'Coficiente 1'],
        ['2', 'Coficiente 2'],
    ]
    nota = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    coeficiente = forms.CharField(widget=forms.Select(attrs={'class':'form-select'}, choices=coeficientes))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}, format='%Y-%m-%d'))

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

    def __init__(self, *args, **kwargs):
        super(AlumnosRegisterForm, self).__init__(*args, **kwargs)
        # self.fields['rut'].required = False
        # self.fields['nombre'].required = False
        # self.fields['apellido_paterno'].required = False
        # self.fields['apellido_materno'].required = False
        # self.fields['fecha_nacimiento'].required = False
        # self.fields['rut_apoderado'].required = False
        # self.fields['sexo'].required = False
        # self.fields['telefono'].required = False
        # self.fields['rut_apoderado'].required = False
        # self.fields['direccion'].required = False
        # self.fields['estado'].required = False



    class Meta:
        model=Alumno
        fields= ('nombre','apellido_paterno','apellido_materno','fecha_nacimiento','rut_apoderado','sexo',
        'telefono','direccion','rut')
        exclude = ('antecedentes',)
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 fw-bold',
                    'placeholder': 'Sin puntos y con guión',
                
                },
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
            # 'estado': forms.Select(
            #     attrs={
            #         'class': 'form-select rounded-pill my-2',   
            #     }
            # ),   
        }

class AlumnoEditForm(AlumnosRegisterForm):
    class Meta:
        model = Alumno
        exclude = ('rut','antecedentes')
        widgets = {
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
                    'class': 'form-select rounded-pill my-2',   
                }
            ),   
        }

class ApoderadosRegisterForm(AlumnosPathern):
    class Meta:
        model=Apoderado
        fields= ('nombre_apoderado','apellido_paterno','apellido_materno','telefono_apoderado','correo','rut')
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

class ApoderadoEditForm(ApoderadosRegisterForm):
    class Meta:
        model = Apoderado
        exclude=('rut',)
        widgets = {
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

 
    