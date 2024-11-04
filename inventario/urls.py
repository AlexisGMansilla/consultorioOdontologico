from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_utensilios, name='lista_utensilios'),  # Ruta para listar utensilios
    path('agregar/', views.agregar_utensilio, name='agregar_utensilio'),  # Ruta para agregar utensilio
]
