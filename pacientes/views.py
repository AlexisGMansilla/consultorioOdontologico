from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente
from django.contrib.auth.decorators import login_required
from .forms import PacienteForm
from django.contrib import messages
from django.http import JsonResponse
import json

@login_required
def pacientes_view(request):
    pacientes = Paciente.objects.all()  # Recupera todos los pacientes
    return render(request, 'pacientes/pacientes.html', {'pacientes': pacientes})

@login_required
def historia_clinica(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los datos del paciente han sido actualizados.')
            return redirect('pacientes:listado')  # Redirige a la lista de pacientes
        else:
            messages.error(request, 'Hubo un error al actualizar los datos.')
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/historia_clinica.html', {'form': form, 'paciente': paciente})

@login_required
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            # Inicializar el odontograma vacío
            paciente.inicializar_odontograma()
            paciente.save()
            messages.success(request, 'El paciente ha sido registrado con éxito.')
            return redirect('pacientes:listado')  # Redirige a la lista de pacientes
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})

@login_required
def ver_odontograma(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        try:
            # Recibe los datos del JSON enviado
            data = json.loads(request.body.decode('utf-8'))
            odontograma_data = data.get('odontograma')

            if odontograma_data:
                paciente.odontograma = odontograma_data
                paciente.save()
                return JsonResponse({'message': 'Odontograma actualizado correctamente.'}, status=200)
            else:
                return JsonResponse({'message': 'Datos del odontograma no proporcionados.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': f'Error al guardar: {str(e)}'}, status=500)

    # Si es un GET, renderiza el odontograma
    if not paciente.odontograma:
        # Inicializa un odontograma vacío si no existe
        paciente.inicializar_odontograma()
        paciente.save()

    return render(request, 'pacientes/ver_odontograma.html', {'paciente': paciente, 'odontograma': paciente.odontograma})
