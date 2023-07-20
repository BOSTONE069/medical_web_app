from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.dispatch import receiver
from django.db.models.signals import pre_delete

# Create your models here.

# The MedicinalPlant class represents a medicinal plant with attributes such as title, treatment,
# prescription, and image.
class MedicinalPlant(models.Model):
    """
    A model representing a medicinal plant.
    """
    title = models.CharField(max_length=100)
    treatment = models.TextField()
    prescription = models.TextField()
    image = models.ImageField(upload_to='luomedicine_app/static/medicinal_plant_images/')

    def __str__(self):
        """
        Returns the title of the medicinal plant.
        """
        return f"{self.title} {self.treatment} {self.prescription}"

    """
    This function deletes the image associated with a MedicinalPlant instance before deleting the
    instance itself.

    :param sender: The `sender` parameter refers to the model class that is sending the signal. In this
    case, it is the `MedicinalPlant` model
    :param instance: The "instance" parameter refers to the instance of the MedicinalPlant model that is
    being deleted. It represents the specific object that is being removed from the database
    """
@receiver(pre_delete, sender=MedicinalPlant)
def medicinal_plant_pre_delete(sender, instance, **kwargs):
    # Check if the image exists and delete it before deleting the instance
    if instance.image and default_storage.exists(instance.image.name):
     default_storage.delete(instance.image.name)


# The Subscribe class represents a model for storing email addresses with uniqueness constraint.
class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        """
        The function saves the object if the email address is valid, otherwise it raises a ValueError.
        """
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValueError("Invalid email address")
        super().save(*args, **kwargs)