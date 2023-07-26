from django.contrib import admin
from .models import MedicinalPlant, Subscribe, LuoFoods, LuoCeremonies, LuoReligion
from .forms import MedicinalPlantForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Register your models here.
# The code `@admin.register(MedicinalPlant)` is a decorator that registers the `MedicinalPlant` model
# with the Django admin site. It tells Django that the `MedicinalPlant` model should be displayed and
# editable in the admin interface.
@admin.register(MedicinalPlant)
class MedicinalPlantAdmin(admin.ModelAdmin):
    form = MedicinalPlantForm
    list_display = ("title", "part", "treatment", "prescription", "image")


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("email",)


@admin.register(LuoFoods)
class LuoFoodsAdmin(admin.ModelAdmin):
    @method_decorator(login_required)
    def get_queryset(self, request):
        return super().get_queryset(request)
    @method_decorator(login_required)
    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj)
    @method_decorator(login_required)
    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj)
    
    list_display = ("title", "description", "image")


@admin.register(LuoReligion)
class ReligionAdmin(admin.ModelAdmin):
    @method_decorator(login_required)
    def get_queryset(self, request):
        return super().get_queryset(request)
    @method_decorator(login_required)
    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj)
    @method_decorator(login_required)
    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj)
    list_display = ("title", "description", "image")
        

@admin.register(LuoCeremonies)
class CeremoniesAdmin(admin.ModelAdmin):
    @method_decorator(login_required)
    def get_queryset(self, request):
        return super().get_queryset(request)
    @method_decorator(login_required)
    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj)
    @method_decorator(login_required)
    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj)
    list_display = ("title", "description", "image")