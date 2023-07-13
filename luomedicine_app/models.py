from django.db import models

# Create your models here.

class MedicinalPlant(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    prescription = models.TextField()
    image = models.ImageField(upload_to='medicinal_plant_images/')

    def __str__(self):
        return self.title
