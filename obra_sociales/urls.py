from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_obras_sociales, name='listar_obras_sociales'),
    path('crear/', views.crear_obra_social, name='crear_obra_social'),
    path('editar/<int:pk>/', views.editar_obra_social, name='editar_obra_social'),
    path('eliminar/<int:obra_id>/', views.eliminar_obra_social, name='eliminar_obra_social'),

]
