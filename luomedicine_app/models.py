from logging import Logger
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.core.exceptions import PermissionDenied

# Create your models here.

# The MedicinalPlant class represents a medicinal plant with attributes such as title, treatment,
# prescription, and image.
class MedicinalPlant(models.Model):
    """
    A model representing a medicinal plant.
    """
    title = models.CharField(max_length=100)
    part = models.TextField(default='leaves')
    treatment = models.TextField()
    prescription = models.TextField()
    image = models.ImageField(upload_to='luomedicine_app/static/medicinal_plant_images/')

    def __str__(self):
        """
        Returns the title of the medicinal plant.
        """
        return f"{self.title} {self.treatment} {self.prescription}"

@receiver(pre_delete, sender=MedicinalPlant)
def medicinal_plant_pre_delete(sender, instance, **kwargs):
    # Check if the user has permission to delete the instance
    if not instance.has_delete_permission():
        raise PermissionDenied("You do not have permission to delete this instance.")
     # Check if the image exists and delete it before deleting the instance
    if instance.image and default_storage.exists(instance.image.name):
        default_storage.delete(instance.image.name)

class LuoFoods(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='luomedicine_app/static/luo_foods/')

    def __str__(self):
        return f"{self.title} {self.description}"
    
@receiver(pre_delete, sender=LuoFoods)
def luo_foods_delete(sender, instance, **kwargs):
    if not instance.has_delete_permission():
        raise PermissionDenied("You do not have the permission to delete the instance.")
    if instance.image and instance.image.name and default_storage.exists(instance.image.name):
        default_storage.delete(instance.image.name)
        Logger.info(f"Image {instance.image.name} has been deleted.")

# The Subscribe class represents a model for storing email addresses with uniqueness constraint.
class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        """
        The function saves the object if the email address is valid, otherwise it raises a ValueError.
# The `try` block is used to handle exceptions that may occur when validating the email address in the
# `save` method of the `Subscribe` model.
        """
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValueError("Invalid email address")
        super().save(*args, **kwargs)