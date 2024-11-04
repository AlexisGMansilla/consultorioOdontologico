from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_register_view, name='login'),  # Login y registro
    path('home/', views.home, name='home'),  # Página de inicio
]
