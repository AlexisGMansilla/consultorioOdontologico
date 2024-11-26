from django.shortcuts import render, redirect, get_object_or_404
from .models import Utensilio
from .forms import UtensilioForm
from django.http import JsonResponse

def lista_utensilios(request):
    utensilios = Utensilio.objects.all()
    form = UtensilioForm()
    return render(request, 'inventario/lista_utensilios.html', {'utensilios': utensilios, 'form': form})

def agregar_utensilio(request):
    if request.method == 'POST':
        form = UtensilioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_utensilios')
    else:
        form = UtensilioForm()
    return render(request, 'inventario/lista_utensilios.html', {'form': form})

def eliminar_utensilio(request, id):
    if request.method == 'POST':
        utensilio = get_object_or_404(Utensilio, id=id)
        utensilio.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Método no permitido'}, status=405)
    
def editar_utensilio(request):
    if request.method == 'POST':
        utensilio_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')

        utensilio = get_object_or_404(Utensilio, id=utensilio_id)
        utensilio.nombre = nombre
        utensilio.cantidad = cantidad
        utensilio.save()

        return redirect('inventario')  # Redirige a la página principal de inventario
