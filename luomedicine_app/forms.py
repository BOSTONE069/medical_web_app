from django import forms
from .models import MedicinalPlant

class MedicinalPlantForm(forms.ModelForm):
    class Meta:
        model = MedicinalPlant
        fields = ['title', 'description', 'prescription', 'image']
