from django.urls import path
from . import views

app_name = 'inventario'  # Define el nombre del namespace

urlpatterns = [
    path('', views.lista_utensilios, name='lista_utensilios'),  # Ruta para listar utensilios
    path('agregar/', views.agregar_utensilio, name='agregar_utensilio'),  # Ruta para agregar utensilio
    path('editar/<int:id>/', views.editar_utensilio, name='editar_utensilio'),  # Ruta para editar utensilios
    path('', views.lista_utensilios, name='inventario'),  # URL principal del inventario
    path('eliminar_utensilio/<int:id>/', views.eliminar_utensilio, name='eliminar_utensilio'),
]
