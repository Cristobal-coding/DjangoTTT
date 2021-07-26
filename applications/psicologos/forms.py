from django import forms
from .models import Informe

class InformeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InformeForm, self).__init__(*args, **kwargs)
        self.fields['pruebas_aplicadas'].required = False
        self.fields['comentario'].required = False
        self.fields['motivo'].required = False

    class Meta:
        model=Informe
        fields= ('rut_alumno', 'fecha_emision','pruebas_aplicadas','comentario','motivo')
        widgets={
            'rut_alumno' : forms.Select(
                attrs={
                    'class' : 'form-select'
                }
            ),
            # 'rut_psicologo' : forms.Select(
                
            #     attrs={
            #         'class' : 'form-select readonly',
            #         'disabled' : 'true'
            #     }
                
            # ),
            'fecha_emision' : forms.DateInput(
                attrs={
                    'class' : 'form-control rounded-pill',
                    'type': 'date'
                }
            ),
       
            
        }