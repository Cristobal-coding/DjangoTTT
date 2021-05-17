from django import forms
from applications.logicas import validar_rut
from applications.users.models import User
from applications.errors import DivErrorList
class LoginForm(forms.Form):
    rut = forms.CharField(
        label='Rut:',
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class': 'form-control border-0 bg-light',
                    'id': 'rut',
                    'placeholder': 'rut'
                    
                }
            ),
    )
    password = forms.CharField(
        label='Contraseña:',
        required=True,
        widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control form-control-sm text-primary bg-light border-0',
                    'id': 'password',
                    'placeholder': 'password'
                }
            ),
    )
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(LoginForm, self).__init__(*args, **kwargs_new)
    def clean_rut(self):
        if self.cleaned_data.get("rut").isdigit():
            if not validar_rut(self.cleaned_data.get("rut")):
                self.add_error('rut', 'Rut no valido')
        return self.cleaned_data.get("rut")