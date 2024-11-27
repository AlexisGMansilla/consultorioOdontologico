import calendar
from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Turno, Paciente
from .forms import TurnoForm
import locale  # Importamos locale para configuraciones de idioma


def vista_calendario(request, year=None, month=None):
    # Establecer el idioma en español para mostrar los nombres de los meses correctamente
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura según tu sistema operativo
    except locale.Error:
        pass  # En algunos sistemas, esto puede no estar disponible

    # Obtener el año y mes actuales si no se proporcionan
    if not year:
        year = datetime.now().year
    if not month:
        month = datetime.now().month

    # Convertir a enteros (por si vienen como strings desde la URL)
    year = int(year)
    month = int(month)

    # Crear el calendario del mes
    cal = calendar.Calendar()
    dias_del_mes = cal.itermonthdays(year, month)

    # Obtener todos los turnos del mes actual
    turnos = Turno.objects.filter(fecha__year=year, fecha__month=month)

    # Generar el nombre del mes en español
    nombre_mes = datetime(year, month, 1).strftime('%B').capitalize()

    # Crear la estructura del calendario
    dias = []
    for dia in dias_del_mes:
        if dia != 0:
            # Obtener los turnos de este día
            turnos_del_dia = turnos.filter(fecha__day=dia)
            dias.append((dia, turnos_del_dia))
        else:
            dias.append((None, None))

    # Pasar los datos al template
    return render(request, 'turnos/calendario.html', {
        'year': year,
        'month': month,
        'dias': dias,
        'nombre_mes': nombre_mes,
        'mes_anterior': month - 1 if month > 1 else 12,
        'mes_siguiente': month + 1 if month < 12 else 1,
        'year_anterior': year if month > 1 else year - 1,
        'year_siguiente': year if month < 12 else year + 1,
    })



def agregar_turno(request, year, month, day):
    # Aseguramos que el día siempre esté representado con dos dígitos
    day = str(day).zfill(2)

    # Inicializar la fecha para usarla en el formulario y en la lógica
    fecha_inicial = date(year, month, int(day))

    # Obtén los pacientes desde el modelo
    pacientes = Paciente.objects.all()  # Asegúrate de tener pacientes en tu base de datos

    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir al calendario después de guardar
            return redirect('turnos:vista_calendario', year=year, month=month)
    else:
        # Establecer la fecha inicial del formulario
        form = TurnoForm(initial={'fecha': fecha_inicial})

    return render(request, 'turnos/agregar_turno.html', {
        'form': form,
        'pacientes': pacientes,  # Pasar pacientes al contexto
        'year': year,
        'month': month,
        'day': day,  # Incluye el día en el contexto
    })



def editar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('turnos:vista_calendario', year=turno.fecha.year, month=turno.fecha.month)
    else:
        form = TurnoForm(instance=turno)
    return render(request, 'turnos/editar_turno.html', {
        'form': form,
        'turno': turno,  # Pasamos el turno actual para acceder a sus datos en el template
    })



def eliminar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)
    year, month = turno.fecha.year, turno.fecha.month
    turno.delete()
    return redirect('turnos:vista_calendario', year=year, month=month)
