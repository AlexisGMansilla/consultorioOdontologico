from django import forms
from .models import ObraSocial

class ObraSocialForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = ['nombre', 'cobertura']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if ObraSocial.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('El nombre ya está registrado.')
        return nombre

    def clean_cobertura(self):
        cobertura = self.cleaned_data.get('cobertura')
        if ObraSocial.objects.filter(cobertura=cobertura).exists():
            raise forms.ValidationError('La cobertura ya está registrada.')
        return cobertura
