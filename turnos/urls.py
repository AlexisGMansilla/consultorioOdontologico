from django.urls import path
from . import views

app_name = 'turnos'
urlpatterns = [
    path('calendario/', views.vista_calendario, name='vista_calendario'),
    path('agregar/<int:year>/<int:month>/<int:day>/', views.agregar_turno, name='agregar_turno'),
    path('editar/<int:turno_id>/', views.editar_turno, name='editar_turno'),
    path('eliminar/<int:turno_id>/', views.eliminar_turno, name='eliminar_turno'),
]
