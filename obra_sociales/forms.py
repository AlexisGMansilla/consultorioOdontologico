from django import forms
from .models import ObraSocial

class ObraSocialForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = ['nombre', 'cobertura']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Excluir la instancia actual si está en edición
        if ObraSocial.objects.filter(nombre=nombre).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('El nombre ya está registrado.')
        return nombre
