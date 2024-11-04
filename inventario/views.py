from django.shortcuts import render, redirect
from .models import Utensilio
from .forms import UtensilioForm

def lista_utensilios(request):
    utensilios = Utensilio.objects.all()
    form = UtensilioForm()
    return render(request, 'inventario/lista_utensilios.html', {'utensilios': utensilios, 'form': form})

def agregar_utensilio(request):
    if request.method == 'POST':
        form = UtensilioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_utensilios')  # Redirige a la lista después de guardar
    else:
        form = UtensilioForm()
    return render(request, 'inventario/lista_utensilios.html', {'form': form})
