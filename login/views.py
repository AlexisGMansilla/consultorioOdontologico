from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

def home(request):
    return render(request, 'home.html')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        error_messages = {
            'username': {
                'required': "Este campo es obligatorio.",
                'unique': "Este nombre de usuario ya está en uso.",
                'max_length': "El nombre de usuario no puede superar los 150 caracteres.",
            },
            'password1': {
                'password_too_similar': "La contraseña no puede ser similar a su otra información personal.",
                'password_too_short': "La contraseña debe contener al menos 8 caracteres.",
                'password_too_common': "La contraseña es demasiado común.",
                'password_entirely_numeric': "La contraseña no puede ser únicamente numérica.",
            },
        }

def login_register_view(request):
    form = CustomUserCreationForm()

    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    elif request.method == 'POST' and 'register' in request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario creado con éxito! Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Hubo un problema al registrar el usuario.')

    return render(request, 'login/login_register.html', {'form': form})
