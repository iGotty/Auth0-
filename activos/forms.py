from django import forms
from .models import Activo

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = [
            'variable',
            'nombre',
            'valor',
            'unit',
            'cantidad',
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            'nombre' : 'Nombre',
            'valor' : 'valor',
            'unit' : 'Unit',
            'cantidad' : 'Cantidad',
            #'dateTime' : 'Date Time',
        }
