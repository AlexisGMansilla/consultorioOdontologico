import calendar
from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Turno, Paciente
from .forms import TurnoForm
import locale  # Importamos locale para configuraciones de idioma
from datetime import date
from django.contrib import messages




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
    fecha_hoy = date.today().strftime('%Y-%m-%d')  # Fecha de hoy
    fecha_inicial = date(year, month, day).strftime('%Y-%m-%d')  # Fecha seleccionada

    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Turno agendado correctamente.")
            return redirect('turnos:vista_calendario', year=year, month=month)
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = TurnoForm(initial={'fecha': fecha_inicial})

    pacientes = Paciente.objects.all()
    return render(request, 'turnos/agregar_turno.html', {
        'form': form,
        'pacientes': pacientes,
        'fecha_hoy': fecha_hoy,
        'fecha_inicial': fecha_inicial,
        'year': year,
        'month': month,
        'day': day,
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
