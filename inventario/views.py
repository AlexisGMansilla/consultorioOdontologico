from django.shortcuts import render, redirect, get_object_or_404
from .models import Utensilio
from .forms import UtensilioForm
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages



def lista_utensilios(request):
    utensilios = Utensilio.objects.all()  # Obtén todos los utensilios
    return render(request, 'inventario/lista_utensilios.html', {'utensilios': utensilios})

def agregar_utensilio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')

        # Guarda el utensilio en la base de datos
        nuevo_utensilio = Utensilio(nombre=nombre, cantidad=cantidad)
        nuevo_utensilio.save()

        # Redirige de nuevo a la lista de utensilios
        return redirect('inventario:lista_utensilios')

    # Renderiza el formulario si el método es GET
    return render(request, 'inventario/agregar_utensilio.html')

def eliminar_utensilio(request, id):
    if request.method == 'POST':
        utensilio = get_object_or_404(Utensilio, id=id)
        utensilio.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Método no permitido'}, status=405)
    
def editar_utensilio(request, id):
    utensilio = get_object_or_404(Utensilio, id=id)
    if request.method == 'POST':
        # Cantidad antes de la edición
        cantidad_anterior = utensilio.cantidad

        # Actualizar datos
        utensilio.nombre = request.POST['nombre']
        nueva_cantidad = int(request.POST['cantidad'])
        utensilio.cantidad = nueva_cantidad

        # Calcular la diferencia en usos
        diferencia = cantidad_anterior - nueva_cantidad
        if diferencia > 0:
            utensilio.usos += diferencia  # Incrementa los usos si se reduce la cantidad

        utensilio.save()
        messages.success(request, "Utensilio actualizado correctamente.")
        return redirect('inventario:lista_utensilios')
