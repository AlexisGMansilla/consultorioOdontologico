from django.db import models

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=20, unique=True)  # Evita duplicados en "nombre"
    cobertura = models.CharField(
        max_length=50,
        choices=[
            ('Familiar', 'Familiar'),
            ('Parcial', 'Parcial'),
            ('Total', 'Total'),
            ('Individual', 'Individual'),
            ('Duo', 'Duo'),
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre'], name='unique_nombre'),
        ]

    def __str__(self):
        return self.nombre
