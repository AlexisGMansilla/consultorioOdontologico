from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.pacientes_view, name='listado'),
    path('historia/<int:paciente_id>/', views.historia_clinica, name='historia_clinica'),
    path('crear/', views.crear_paciente, name='crear_paciente'),
    path('<int:paciente_id>/odontograma/', views.ver_odontograma, name='ver_odontograma'),
    path('guardar-odontograma/<int:paciente_id>/', views.guardar_odontograma, name='guardar_odontograma'),
    path('cargar-odontograma/<int:paciente_id>/', views.cargar_odontograma, name='cargar_odontograma'),

]
