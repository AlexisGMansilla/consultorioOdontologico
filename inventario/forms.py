from django import forms
from .models import Utensilio

class UtensilioForm(forms.ModelForm):
    class Meta:
        model = Utensilio
        fields = ['nombre', 'cantidad']
