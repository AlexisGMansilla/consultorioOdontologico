from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_utensilios, name='lista_utensilios'),  # Ruta para listar utensilios
    path('agregar/', views.agregar_utensilio, name='agregar_utensilio'),  # Ruta para agregar utensilio
    path('', views.lista_utensilios, name='inventario'),  # URL principal del inventario
    path('eliminar_utensilio/<int:id>/', views.eliminar_utensilio, name='eliminar_utensilio'),
    path('editar_utensilio/', views.editar_utensilio, name='editar_utensilio'),
]
