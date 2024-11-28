from datetime import datetime, date, time
from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['paciente', 'fecha', 'hora', 'motivo']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        hora = cleaned_data.get('hora')
        fecha = cleaned_data.get('fecha')

        # Validación de franjas horarias
        if hora < time(8, 0) or (hora > time(12, 0) and hora < time(15, 0)) or hora > time(20, 0):
            raise forms.ValidationError(
                "El horario permitido es de 8:00 a 12:00 y de 15:00 a 20:00."
            )

        # Validación para no permitir fechas pasadas
        if fecha and fecha < date.today():
            raise forms.ValidationError("No se pueden asignar turnos en fechas pasadas.")


        return cleaned_data
