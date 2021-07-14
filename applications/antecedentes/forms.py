from django import forms
from applications.errors import DivErrorList
from .models import Alumno, Antecedente, Apoderado
from django.forms import ValidationError

# class AntecedenteForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AntecedenteForm, self).__init__(*args, **kwargs)
#         self.fields['nombre_antecedente'].label = "Nombre del antecedente:"

#     def clean_nombre(self):
#         nombre = self.cleaned_data['nombre_antecedente']
#         existe = Antecedente.objects.filter(nombre_antecedente__iexact=nombre).exists()

#         if existe:
#             self.fields['nombre_antecedente'].widget.attrs.update({'class': 'form-control rounded-pill my-2 text-capitalize is-invalid'})
#             raise ValidationError('Esta nombre ya esta utilizado')
#         return nombre

