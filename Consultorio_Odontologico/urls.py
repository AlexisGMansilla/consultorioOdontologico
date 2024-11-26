from django.contrib import admin
from django.urls import path, include
from . import views  # Importa el nuevo views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', views.home, name='home'), 
    path('pacientes/', include('pacientes.urls', namespace='pacientes')),
    path('inventario/', include('inventario.urls', namespace='inventario')),
    path('turnos/', include('turnos.urls', namespace='turnos')),
    path('login/', include('login.urls', namespace='login')),

]
