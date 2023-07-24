from django import forms
from .models import MedicinalPlant, Subscribe, LuoFoods

# The `MedicinalPlantForm` class is a model form for the `MedicinalPlant` model with fields for title,
# treatment, prescription, and image.
class MedicinalPlantForm(forms.ModelForm):
    class Meta:
        model = MedicinalPlant
        fields = ['title', 'part', 'treatment', 'prescription', 'image']


# The `SubscriptionForm` class is a model form that allows users to subscribe by entering their email
# address.
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']

class LuoFoodsForm(forms.ModelForm):
    class Meta:
        model = LuoFoods
        fields = ['title', 'description', 'image']