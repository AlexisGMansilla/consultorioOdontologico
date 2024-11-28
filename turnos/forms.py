from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['paciente', 'fecha', 'hora', 'motivo']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')

        if Turno.objects.filter(fecha=fecha, hora=hora).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un turno asignado para esta fecha y hora.')

        return cleaned_data