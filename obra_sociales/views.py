from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import ObraSocialForm
from .models import ObraSocial

def listar_obras_sociales(request):
    obras = ObraSocial.objects.all()  # Obtiene todas las obras sociales
    return render(request, 'obra_sociales/listar_obras.html', {'obras': obras})

def crear_obra_social(request):
    if request.method == 'POST':
        form = ObraSocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obra_sociales:listar_obras_sociales')  # Usa el namespace definido
    else:
        form = ObraSocialForm()
    return render(request, 'obra_sociales/crear_obra_social.html', {'form': form})

def editar_obra_social(request, pk):
    obra = get_object_or_404(ObraSocial, pk=pk)
    if request.method == 'POST':
        form = ObraSocialForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('obra_sociales:listar_obras_sociales')  # Usa el namespace definido
    else:
        form = ObraSocialForm(instance=obra)
    return render(request, 'obra_sociales/editar_obra_social.html', {'form': form, 'obra': obra})

def eliminar_obra_social(request, obra_id):
    if request.method == 'POST':  # Asegúrate de que solo acepta POST
        obra = get_object_or_404(ObraSocial, id=obra_id)
        obra.delete()
        return JsonResponse({'message': 'Obra social eliminada correctamente.'})  # Respuesta JSON
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

def validar_nombre(request):
    nombre = request.GET.get('nombre', None)
    valido = not ObraSocial.objects.filter(nombre=nombre).exists()
    return JsonResponse({'valido': valido})
