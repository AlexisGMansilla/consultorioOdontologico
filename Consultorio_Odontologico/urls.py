from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para acceder al panel de administración
    path('login/', include('login.urls')),  # Incluye las URLs de la app login
    path('pacientes/', include('pacientes.urls')),  # Incluye las URLs de la app pacientes
    path('', RedirectView.as_view(url='/login/', permanent=True)),  # Redirecciona la raíz del sitio a la página de login
]
