from django.urls import path
from . import views

app_name = 'obra_sociales'  # Namespace para las URLs de esta app

urlpatterns = [
    path('', views.listar_obras_sociales, name='listar_obras_sociales'),  # Nombre correcto
    path('crear/', views.crear_obra_social, name='crear_obra_social'),
    path('editar/<int:pk>/', views.editar_obra_social, name='editar'),
    path('eliminar/<int:obra_id>/', views.eliminar_obra_social, name='eliminar'),
]
