# pacientes/admin.py
from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'edad', 'telefono', 'genero', 'email')
    search_fields = ('nombre', 'apellido', 'dni', 'telefono')
    list_filter = ('genero',)

    def edad(self, obj):
        return obj.edad
    edad.short_description = 'Edad'
