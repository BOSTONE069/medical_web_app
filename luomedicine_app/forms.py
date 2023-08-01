from django import forms
from .models import MedicinalPlant, Subscribe, LuoFoods, LuoReligion, LuoCeremonies


# The `MedicinalPlantForm` class is a model form for the `MedicinalPlant` model with fields for title,
# treatment, prescription, and image.
class MedicinalPlantForm(forms.ModelForm):
    class Meta:
        model = MedicinalPlant
        fields = ["title", "part", "treatment", "prescription", "image"]


# The `SubscriptionForm` class is a model form that allows users to subscribe by entering their email
# address.
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ["email"]


# The `LuoFoodsForm` class is a model form that allows users to create instances of the `LuoFoods`
# model with fields for title, description, and image.
class LuoFoodsForm(forms.ModelForm):
    class Meta:
        model = LuoFoods
        fields = ["title", "description", "image"]


# The class `LuoReligionForm` is a model form for the `LuoReligion` model with fields for `title`,
# `description`, and `image`.
class LuoReligionForm(forms.ModelForm):
    class Meta:
        model = LuoReligion
        fields = ["title", "description", "image"]


# The class LuoCeremoniesForm is a ModelForm that is used to create a form for the LuoCeremonies model
# with fields for title, description, and image.
class LuoCeremoniesForm(forms.ModelForm):
    class Meta:
        model = LuoCeremonies
        fields = ["title", "description", "image"]
