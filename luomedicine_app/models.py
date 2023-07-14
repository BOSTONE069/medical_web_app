from django.db import models

# Create your models here.

class MedicinalPlant(models.Model):
    """
    A model representing a medicinal plant.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    prescription = models.TextField()
    image = models.ImageField(upload_to='medicinal_plant_images/')

    def __str__(self):
        """
        Returns the title of the medicinal plant.
        """
        return self.title
