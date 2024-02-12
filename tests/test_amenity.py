"""
Module to test the Amenity class functionality.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up a test instance of the Amenity class.
        """
        self.amenity = Amenity(name="WiFi")

    def test_attributes(self):
        """
        Test that the attributes of the Amenity instance are correctly set.
        """
        self.assertEqual(self.amenity.name, "WiFi")

    def test_default_values(self):
        """
        Test that default values are correctly
            set when no arguments are passed.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_optional_name(self):
        """
        Test that optional name argument can be passed correctly.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")


if __name__ == "__main__":
    unittest.main()
