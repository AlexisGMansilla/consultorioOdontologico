from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente  # Asegúrate de tener el modelo Paciente o ajusta el nombre según tu modelo
from django.contrib.auth.decorators import login_required
from .forms import PacienteForm

@login_required
def pacientes_view(request):
    pacientes = Paciente.objects.all()  # Recupera todos los pacientes
    return render(request, 'pacientes/pacientes.html', {'pacientes': pacientes})

def historia_clinica(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'pacientes/historia_clinica.html', {'paciente': paciente})

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes')  # Redirige a la lista de pacientes después de crear uno nuevo
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})