"""
Module to test the functionality of the City class.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up a test instance of the City class.
        """
        self.city = City(state_id="CA", name="San Francisco")

    def test_attributes(self):
        """
        Test that the attributes of the City instance are correctly set.
        """
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_default_values(self):
        """
        Test that default values are correctly set when no arguments are pased
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_optional_values(self):
        """
        Test that optional state_id and name arguments can be passed correctly
        """
        # Test with state_id only
        city = City(state_id="NY")
        self.assertEqual(city.state_id, "NY")
        self.assertEqual(city.name, "")

        # Test with name only
        city = City(name="Los Angeles")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "Los Angeles")

        # Test with no arguments
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
