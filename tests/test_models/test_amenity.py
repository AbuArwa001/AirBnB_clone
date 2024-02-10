import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity(name="WiFi")

    def test_attributes(self):
        self.assertEqual(self.amenity.name, "WiFi")

    def test_default_values(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_optional_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")


if __name__ == '__main__':
    unittest.main()
