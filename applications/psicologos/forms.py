from django import forms
from .models import Informe

class InformeForm(forms.ModelForm):
    class Meta:
        model=Informe
        fields= ('__all__')
        widgets={
            'rut_alumno' : forms.Select(
                attrs={
                    'class' : 'form-select'
                }
            ),
            'rut_psicologo' : forms.Select(
                
                attrs={
                    'class' : 'form-select readonly',
                    'disabled' : 'true'
                }
                
            ),
            'fecha_emision' : forms.DateInput(
                attrs={
                    'class' : 'form-control rounded-pill',
                    'type': 'date'
                }
            ),
       
            
        }