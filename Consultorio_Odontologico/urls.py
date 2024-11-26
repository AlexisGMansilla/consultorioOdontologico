from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),  
    path('pacientes/', include('pacientes.urls')),
    path('', RedirectView.as_view(url='/login/', permanent=True)), 
    path('inventario/', include('inventario.urls')), 
    path('turnos/', include('turnos.urls')), 
]
