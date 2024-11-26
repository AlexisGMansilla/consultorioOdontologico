# pacientes/models.py
from django.db import models
from datetime import date

class Paciente(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15, blank=True) 
    direccion = models.CharField(max_length=255)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True)
    observacion = models.TextField(blank=True)
    odontograma = models.JSONField(default=dict) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def inicializar_odontograma(self):
        # Generar un odontograma vacío por defecto
        cuadrantes = {
            "superior_izquierdo": [{"numero": i, "estado": "Sano"} for i in range(18, 10, -1)],
            "superior_derecho": [{"numero": i, "estado": "Sano"} for i in range(21, 29)],
            "inferior_izquierdo": [{"numero": i, "estado": "Sano"} for i in range(48, 40, -1)],
            "inferior_derecho": [{"numero": i, "estado": "Sano"} for i in range(31, 39)],
        }
        self.odontograma = cuadrantes

    @property
    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
