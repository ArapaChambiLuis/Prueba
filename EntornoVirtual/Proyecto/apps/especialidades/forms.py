from django import forms
from apps.especialidades.models import Persona, Experiencia, PerProfesion , Capacitacion



class formP(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre','dni',
        ]
        labels = {
            'nombre':'Apellidos y nombres',
            'dni':'Dni'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }

class form_verDetalles(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre', 'dni',
        ]
        labels = {
            'nombre': 'Apellidos y nombres',
            'dni': 'Dni',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'dni': forms.TextInput(),
        }

class form_Experiencia(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = [
            'CodPers',
            'LugarTrabajo',
            'DesTrabajo',
            'FecIni',
            'FecFin',
            'NroConv',
            'Contrato',
            'MotivoRetiro',
            'CodProf',
            'Vigente'
        ]
        labels = {
            'CodPers': 'Persona',
            'LugarTrabajo' :'Lugar de trabajo' ,
            'DesTrabajo':'Descripcion de trabajo',
            'FecIni':'Fecha de inicio',
            'FecFin':'Fecha de fin',
            'NroConv': 'Numero de convocatoria',
            'Contrato': 'Tipo de contrato',
            'MotivoRetiro':'Motivo de retiro',
            'CodProf': 'Profesion ejercida',
            'Vigente' : '¿Se encuentra vigente?'
        }
        widgets = {
            'CodPers' : forms.Select(attrs={'class': 'form-control'}),
            'LugarTrabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'DesTrabajo': forms.Textarea(attrs={'class': 'form-control'}),
            'FecIni' : forms.DateInput(attrs={'class': 'form-control'}),
            'FecFin' : forms.DateInput(attrs={'class': 'form-control'}),
            'NroConv' : forms.TextInput(attrs={'class': 'form-control'}),
             'Contrato' :forms.TextInput(attrs={'class': 'form-control'}),
             'MotivoRetiro': forms.TextInput(attrs={'class': 'form-control'}),
             'CodProf': forms.Select(attrs={'class': 'form-control'}),
             'Vigente' : forms.Select(attrs={'class': 'form-control'}),
        }

class form_PerProfesion(forms.ModelForm):
    class Meta :
        model=PerProfesion
        fields = [
            'CodPers',
            'CodProf',
            'CodCentEst',
            'NroCIP',
            'FecCIPVig',
            'Vigente',
        ]
        labels = {
            'CodPers' : 'Persona',
            'CodProf' : 'Profesion obtenida',
            'CodCentEst' : '¿Donde estudio?',
            'NroCIP' : 'Codigo institucional',
            'FecCIPVig' : 'Fecha de vigencia del codigo institucional',
            'Vigente': '¿Se encuentra vigente el codigo?',
        }
        widgets = {
            'CodPers' : forms.Select(attrs={'class': 'form-control'}),
            'CodProf': forms.Select(attrs={'class': 'form-control'}),
            'CodCentEst': forms.Select(attrs={'class': 'form-control'}),
            'NroCIP': forms.TextInput(attrs={'class': 'form-control'}),
            'FecCIPVig': forms.DateInput(attrs={'class': 'form-control'}),
            'Vigente': forms.Select(attrs={'class': 'form-control'}),
        }

class form_act_profesion(forms.ModelForm):
    class Meta :
        model=PerProfesion
        fields = [
            'CodProf',
            'CodCentEst',
            'NroCIP',
            'FecCIPVig',
            'Vigente',
        ]
        labels = {
            'CodProf' : 'Profesion obtenida',
            'CodCentEst' : '¿Donde estudio?',
            'NroCIP' : 'Codigo institucional',
            'FecCIPVig' : 'Fecha de vigencia del codigo institucional',
            'Vigente': '¿Se encuentra vigente el codigo?',
        }
        widgets = {
            'CodProf': forms.Select(attrs={'class': 'form-control'}),
            'CodCentEst': forms.Select(attrs={'class': 'form-control'}),
            'NroCIP': forms.TextInput(attrs={'class': 'form-control'}),
            'FecCIPVig': forms.DateInput(attrs={'class': 'form-control'}),
            'Vigente': forms.Select(attrs={'class': 'form-control'}),
        }


class form_Capacitacion(forms.ModelForm):
    class Meta :
        model = Capacitacion
        fields = [
            'CodPers',
            'CodCentEst',
            'CodProf',
            'NombreInst',
            'DesCap',
            'FecIni',
            'FecFin',
            'NroHoras',
            'Vigente',



        ]
        labels = {
            'CodPers':'persona',
            'CodCentEst':'Lugar donde se capacito',
            'CodProf':'Nombre de profesion',
            'NombreInst':'Lugar donde se capacito',
            'DesCap':'Descripcion de capacitacion',
            'FecIni':'Fecha de inicio',
            'FecFin':'Fecha de fin',
            'NroHoras':'Numero de horas',
            'Vigente':'¿Se encuentra vigente?',
        }
        widgets = {
            'CodPers':forms.Select(attrs={'class': 'form-control'}),
            'CodCentEst': forms.Select(attrs={'class': 'form-control'}),
            'CodProf': forms.Select(attrs={'class': 'form-control'}),
            'NombreInst': forms.TextInput(attrs={'class': 'form-control'}),
            'DesCap': forms.TextInput(attrs={'class': 'form-control'}),
            'FecIni':forms.DateInput(attrs={'class': 'form-control'}),
            'FecFin':forms.DateInput(attrs={'class': 'form-control'}),
            'NroHoras': forms.TextInput(attrs={'class': 'form-control'}),
            'Vigente': forms.Select(attrs={'class': 'form-control'}),
        }

