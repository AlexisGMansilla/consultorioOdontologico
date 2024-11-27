from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=20)
    alcance = models.CharField(max_length=50, choices=[
        ('Niños', 'Niños'),
        ('Adolescentes', 'Adolescentes'),
        ('Adultos', 'Adultos'),
        ('Jubilados', 'Jubilados'),
        ('Embarazadas', 'Embarazadas'),
        ('Discapacidad', 'Personas con discapacidad'),
    ])
    cobertura = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)  
        ]
    )