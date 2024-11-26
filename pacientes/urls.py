from django.urls import path
from . import views

app_name = 'pacientes'  

urlpatterns = [
    path('', views.pacientes_view, name='listado'),  
    path('historia/<int:paciente_id>/', views.historia_clinica, name='historia_clinica'),
    path('crear/', views.crear_paciente, name='crear_paciente'),
    path('<int:paciente_id>/odontograma/', views.ver_odontograma, name='ver_odontograma'),
]
