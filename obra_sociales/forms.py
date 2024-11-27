from django import forms
from .models import ObraSocial

class ObraSocialForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = ['nombre', 'alcance', 'cobertura']
        widgets = {
            'alcance': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean_cobertura(self):
        cobertura = self.cleaned_data.get('cobertura')
        if cobertura < 1:
            raise forms.ValidationError('La cobertura no puede ser un valor negativo ni 0.')
        return cobertura
