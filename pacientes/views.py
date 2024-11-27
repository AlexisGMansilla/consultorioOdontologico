from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente,DienteEstado
from django.contrib.auth.decorators import login_required
from .forms import PacienteForm
from django.contrib import messages
from django.http import JsonResponse
import json

@login_required
def pacientes_view(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/pacientes.html', {'pacientes': pacientes})

@login_required
def historia_clinica(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los datos del paciente han sido actualizados.')
            return redirect('pacientes:listado')
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
            paciente.inicializar_odontograma()
            paciente.save()
            messages.success(request, 'El paciente ha sido registrado con éxito.')
            return redirect('pacientes:listado')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})

@login_required
def ver_odontograma(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        try:
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

    if not paciente.odontograma:
        paciente.inicializar_odontograma()
        paciente.save()

    # Listas de dientes para pasar al contexto
    dientes_superior_izquierdo = list(range(18, 10, -1))
    dientes_superior_derecho = list(range(21, 29))
    dientes_inferior_izquierdo = list(range(48, 40, -1))
    dientes_inferior_derecho = list(range(31, 39))

    return render(request, 'pacientes/ver_odontograma.html', {
        'paciente': paciente,
        'odontograma': paciente.odontograma,
        'dientes_superior_izquierdo': dientes_superior_izquierdo,
        'dientes_superior_derecho': dientes_superior_derecho,
        'dientes_inferior_izquierdo': dientes_inferior_izquierdo,
        'dientes_inferior_derecho': dientes_inferior_derecho,
    })


def guardar_odontograma(request, paciente_id):
    if request.method == "POST":
        try:
            # Decodificar los datos enviados desde el cliente
            datos = json.loads(request.body)
            paciente = Paciente.objects.get(id=paciente_id)

            for numero_diente, estado in datos.items():
                print(f"Procesando diente {numero_diente}: {estado}")  # Debug
                diente, creado = DienteEstado.objects.update_or_create(
                    paciente=paciente,
                    numero_diente=int(numero_diente),  # Asegurarse de que sea un entero
                    defaults={
                        "cara_arriba": estado.get("arriba", "Sano"),
                        "cara_derecha": estado.get("derecha", "Sano"),
                        "cara_izquierda": estado.get("izquierda", "Sano"),
                        "cara_abajo": estado.get("abajo", "Sano"),
                        "cara_central": estado.get("central", "Sano"),
                    }
                )
                print(f"Diente actualizado o creado: {diente}")
            return JsonResponse({"message": "Estados guardados correctamente."}, status=200)
        except Exception as e:
            print(f"Error al guardar: {e}")  # Debug
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido."}, status=405)


def cargar_odontograma(request, paciente_id):
    try:
        paciente = Paciente.objects.get(id=paciente_id)
        dientes = DienteEstado.objects.filter(paciente=paciente)

        estados = {
            diente.numero_diente: {
                "arriba": diente.cara_arriba,
                "derecha": diente.cara_derecha,
                "izquierda": diente.cara_izquierda,
                "abajo": diente.cara_abajo,
                "central": diente.cara_central,
            }
            for diente in dientes
        }

        return JsonResponse(estados, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
