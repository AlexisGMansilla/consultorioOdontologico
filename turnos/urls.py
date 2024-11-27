from django.urls import path
from django.shortcuts import redirect  # Asegúrate de importar redirect
from . import views
from datetime import datetime

app_name = 'turnos'
urlpatterns = [
    path('<int:year>/<int:month>/', views.vista_calendario, name='vista_calendario'),
    path('agregar/<int:year>/<int:month>/<int:day>/', views.agregar_turno, name='agregar_turno'),
    path('editar/<int:turno_id>/', views.editar_turno, name='editar_turno'),
    path('eliminar/<int:turno_id>/', views.eliminar_turno, name='eliminar_turno'),
]