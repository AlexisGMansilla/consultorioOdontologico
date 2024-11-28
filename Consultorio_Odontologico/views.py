from django.shortcuts import render
from datetime import datetime, date
from turnos.models import Turno  # Asegúrate de importar el modelo de turnos correctamente

def home(request):
    today = date.today()  # Obtén la fecha actual
    # Filtra los turnos de la fecha actual
    turnos_hoy = Turno.objects.filter(fecha=today).order_by('hora')
    
    return render(request, 'home.html', {
        'year': today.year,
        'month': today.month,
        'turnos_hoy': turnos_hoy  # Pasa los turnos al template
    })
