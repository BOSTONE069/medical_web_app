from django.forms import ValidationError
from django.test import TestCase
from .models import MedicinalPlant, LuoCeremonies
import unittest


# Create your tests here.


# The MedicinalPlantTestCase class contains test methods to verify the functionality and attributes of
# the MedicinalPlant model.
class MedicinalPlantTestCase(TestCase):
    def setUp(self):
        self.plant = MedicinalPlant.objects.create(
            title="Plant A",
            treatment="Treatment A",
            prescription="Prescription A",
            image="path/to/image.jpg",
        )

    def test_str(self):
        self.assertEqual(str(self.plant), "Plant A Treatment A Prescription A")

    def test_title_max_length(self):
        max_length = self.plant._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_treatment_blank(self):
        """
        The function creates a MedicinalPlant object with a blank treatment and asserts that the
        treatment is empty.
        """
        plant = MedicinalPlant.objects.create(
            title="Plant B", prescription="Prescription B", image="path/to/image.jpg"
        )
        self.assertEqual(plant.treatment, "")

    def test_prescription_blank(self):
        plant = MedicinalPlant.objects.create(
            title="Plant C", treatment="Treatment C", image="path/to/image.jpg"
        )
        self.assertEqual(plant.prescription, "")

    def test_image_upload_path(self):
        expected_path = "luomedicine_app/static/medicinal_plant_images/image.jpg"
        self.assertEqual(self.plant.image.path, expected_path)


# The `LuoCeremoniesTestCase` class contains test cases for the `LuoCeremonies` class, including
# methods for testing the sanitized description, string representation, image upload, and invalid
# image extension.
class LuoCeremoniesTestCase(unittest.TestCase):
    def setUp(self):
        self.ceremony = LuoCeremonies(
            title="Test Ceremony",
            description="Test Description",
            image="test_image.jpg"
        )

    def test_sanitized_description(self):
        """
        The function `test_sanitized_description` tests the `sanitized_description` method of the
        `ceremony` object.
        """
        self.assertEqual(
            self.ceremony.sanitized_description(),
            "Test Description"
        )

    def test_str_representation(self):
        """
        The function tests the string representation of a Ceremony object.
        """
        self.assertEqual(
            str(self.ceremony),
            "Test Ceremony Test Description"
        )

    def test_image_upload(self):
        self.assertEqual(
            self.ceremony.image.upload_to,
            "luomedicine_app/static/luo_ceremonies/"
        )
        self.assertTrue(
            self.ceremony.image.validators[0].allowed_extensions,
            [".jpg", ".jpeg", ".png", ".gif", ".PNG", ".JPG"]
        )

    def test_invalid_image_extension(self):
        with self.assertRaises(ValidationError):
            self.ceremony.image.clean("test_image.pdf")


if __name__ == "__main__":
    unittest.main()
