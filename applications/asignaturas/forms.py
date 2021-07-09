from applications.cursos.models import PlanEstudio
from django import forms
from .models import Asignatura
from django.forms import ValidationError

class AsignaturaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AsignaturaForm, self).__init__(*args, **kwargs)
        self.fields['cod_asign'].label = "Codigo de la asignatura:"

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = Asignatura.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            self.fields['nombre'].widget.attrs.update({'class': 'form-control rounded-pill my-2 text-capitalize is-invalid'})
            raise ValidationError('Esta nombre ya esta utilizado')
        return nombre

    def clean_cod_asign(self):
        cod = self.cleaned_data['cod_asign']
        existe = Asignatura.objects.filter(cod_asign__iexact=cod).exists()

        if existe:
            self.fields['cod_asign'].widget.attrs.update({'class': 'form-control rounded-pill my-2 text-uppercase is-invalid'})
            raise ValidationError('Esta codigo ya esta ingresado')
        return cod

    class Meta:
        model=Asignatura
        fields= ('__all__')
        widgets={
            'cod_asign': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 text-uppercase',
                    'placeholder': 'Este valor debe ser unico'
                },
                
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-pill my-2 text-capitalize',
                    'placeholder': 'Nombre representativo'
                }
            ),
        }
class PlanesForm(forms.ModelForm):
    class Meta:
        model=PlanEstudio
        fields= ('__all__')
        # widgets={
        #     'cod_asign': forms.TextInput(
        #         attrs={
        #             'class': 'form-control rounded-pill my-2 text-uppercase',
        #             'placeholder': 'Este valor debe ser unico'
        #         },
                
        #     ),
        #     'nombre': forms.TextInput(
        #         attrs={
        #             'class': 'form-control rounded-pill my-2 text-capitalize',
        #             'placeholder': 'Nombre representativo'
        #         }
        #     ),
        # }