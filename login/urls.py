from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.login_register_view, name='login'),  # Login y registro
    path('home/', views.home, name='home'),  # Página de inicio
    path('logout/', LogoutView.as_view(), name='logout'),  # URL para cerrar sesión
]
