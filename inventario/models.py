from django.db import models

class Utensilio(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
