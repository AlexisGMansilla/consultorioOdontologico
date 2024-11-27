from django.core.exceptions import ValidationError
from django.db import models
from pacientes.models import Paciente  # Importar el modelo de pacientes
class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  # Relación con el modelo Paciente
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(blank=True)

    def clean(self):
        # Validar si ya existe un turno con la misma fecha y hora
        if Turno.objects.filter(fecha=self.fecha, hora=self.hora).exclude(pk=self.pk).exists():
            raise ValidationError('Ya existe un turno asignado para esta fecha y hora.')
