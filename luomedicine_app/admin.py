from django.contrib import admin
from .models import MedicinalPlant, Subscribe, LuoFoods
from .forms import MedicinalPlantForm

# Register your models here.
# The code `@admin.register(MedicinalPlant)` is a decorator that registers the `MedicinalPlant` model
# with the Django admin site. It tells Django that the `MedicinalPlant` model should be displayed and
# editable in the admin interface.
@admin.register(MedicinalPlant)
class MedicinalPlantAdmin(admin.ModelAdmin):
    form = MedicinalPlantForm
    list_display = ('title', 'part', 'treatment', 'prescription', 'image')


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("email",)
@admin.register(LuoFoods)
class LuoFoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    