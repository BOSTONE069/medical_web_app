from logging import Logger
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.core.exceptions import PermissionDenied
import os
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.core.validators import FileExtensionValidator


# Create your models here.


# The MedicinalPlant class represents a medicinal plant with attributes such as title, treatment,
# prescription, and image.
class MedicinalPlant(models.Model):
    def validate_image_file_extension(value):
        allowed_extensions = [".jpg", ".jpeg", ".png", ".gif", ".PNG", ".JPG"]
        ext = os.path.splitext(value.name)[1]
        if not ext.lower() in allowed_extensions:
            raise ValidationError(
                "Unsupported file extension.  Allowed extensions are: .jpg, .jpeg, .png, .gif"
            )

    """
    A model representing a medicinal plant.
    """
    title = models.CharField(max_length=100)
    part = models.TextField(default="leaves")
    treatment = models.TextField()
    prescription = models.TextField()
    image = models.ImageField(
        upload_to="luomedicine_app/static/medicinal_plant_images/",
        validators=[validate_image_file_extension],
    )

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
    def validate_image_file_extension(value):
        allowed_extensions = [".jpg", ".jpeg", ".png", ".gif", ".PNG", ".JPG"]
        ext = os.path.splitext(value.name)[1]
        if not ext.lower() in allowed_extensions:
            raise ValidationError("Unsupported file extension.")

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to="luomedicine_app/static/luo_foods/",
        validators=[validate_image_file_extension],
    )

    def __str__(self):
        return f"{self.title} {self.description}"

    """
    The above function is a pre-delete signal receiver in Django that checks if the user has permission
    to delete an instance of the LuoFoods model, and if so, deletes the associated image file and logs
    the deletion.
    
    :param sender: The `sender` parameter refers to the model class that is sending the signal. In this
    case, the `sender` is `LuoFoods`, which is a Django model
    :param instance: The `instance` parameter refers to the instance of the `LuoFoods` model that is
    being deleted. It represents the specific object that is being removed from the database
    """


@receiver(pre_delete, sender=LuoFoods)
def luo_foods_delete(sender, instance, **kwargs):
    if not instance.has_delete_permission():
        raise PermissionDenied("You do not have the permission to delete the instance.")
    if (
            instance.image
            and instance.image.name
            and default_storage.exists(instance.image.name)
    ):
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


# The `LuoReligion` class represents a model for storing information about Luo religion, including a
# title, description, and image.
class LuoReligion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="luomedicine_app/static/luo_religion/")

    def __str__(self):
        return f"{self.title} {self.description}"


# The `LuoCeremonies` class represents ceremonies in the Luo culture, with attributes for title,
# description, and image.
class LuoCeremonies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to="luomedicine_app/static/luo_ceremonies/",
        validators=[FileExtensionValidator([".jpg", ".jpeg", ".png", ".gif", ".PNG", ".JPG"])]
    )

    @property
    def sanitized_description(self):
        return mark_safe(escape(self.description))

    def __str__(self):
        return f"{self.title} {self.sanitized_description}"
