from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['paciente', 'fecha', 'hora', 'motivo']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TextInput(attrs={'class': 'timepicker'}), 
        }
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')

        if Turno.objects.filter(fecha=fecha, hora=hora).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un turno asignado para esta fecha y hora.')

        return cleaned_data