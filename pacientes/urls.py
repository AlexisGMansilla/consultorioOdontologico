from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes_view, name='pacientes'),
    path('historia/<int:paciente_id>/', views.historia_clinica, name='historia_clinica'),
    path('crear/', views.crear_paciente, name='crear_paciente'),  # URL para crear paciente
]
