from django.test import TestCase
from .models import MedicinalPlant
# Create your tests here.

class MedicinalPlantTestCase(TestCase):
    def setUp(self):
        self.plant = MedicinalPlant.objects.create(
            title="Plant A",
            treatment="Treatment A",
            prescription="Prescription A",
            image="path/to/image.jpg"
        )
    def test_str(self):
        self.assertEqual(str(self.plant), "Plant A Treatment A Prescription A")
    def test_title_max_length(self):
        max_length = self.plant._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)
    def test_treatment_blank(self):
        plant = MedicinalPlant.objects.create(
            title="Plant B",
            prescription="Prescription B",
            image="path/to/image.jpg"
        )
        self.assertEqual(plant.treatment, "")
    def test_prescription_blank(self):
        plant = MedicinalPlant.objects.create(
            title="Plant C",
            treatment="Treatment C",
            image="path/to/image.jpg"
        )
        self.assertEqual(plant.prescription, "")
    def test_image_upload_path(self):
        expected_path = 'luomedicine_app/static/medicinal_plant_images/image.jpg'
        self.assertEqual(self.plant.image.path, expected_path)