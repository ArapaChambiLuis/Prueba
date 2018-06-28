from django import forms
from apps.especialidades.models import Persona, Experiencia, PerProfesion


class formP(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre','dni'
        ]
        labels = {
            'nombre':'Apellidos y nombres',
            'dni':'Dni'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }



