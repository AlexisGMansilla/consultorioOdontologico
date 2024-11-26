# login/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'login'

urlpatterns = [
    path('', views.login_register_view, name='login'),  
    path('logout/', LogoutView.as_view(next_page='login:login'), name='logout'), 
]
