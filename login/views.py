from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Formulario personalizado para el registro de usuarios
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar los mensajes de error y las etiquetas
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Correo Electrónico'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar Contraseña'})

def login_register_view(request):
    """
    Vista combinada para manejar el inicio de sesión y el registro en la misma página.
    """
    form = CustomUserCreationForm()

    # Manejo de inicio de sesión
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Por favor, completa ambos campos para iniciar sesión.')
            return render(request, 'login_register.html', {'form': form})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')  # Redirige a la página de pacientes
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'login_register.html', {'form': form})

    # Manejo de registro de usuario
    elif request.method == 'POST' and 'register' in request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario registrado con éxito! Ahora puedes iniciar sesión.')
            return redirect('login:login')  # Redirige a la vista de login
        else:
            messages.error(request, 'Hubo un problema al registrar el usuario.')
            return render(request, 'login_register.html', {'form': form})

    # Renderiza el formulario si el método no es POST
    return render(request, 'login_register.html', {'form': form})
