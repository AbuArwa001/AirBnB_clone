"""
Module to test the functionality of the Place class.
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up a test instance of the Place class.
        """
        self.place = Place(
            city_id="1",
            user_id="user123",
            name="Example Place",
            description="A cozy place for vacation",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100.00,
            latitude=40.7128,
            longitude=-74.0060,
            amenity_ids=[1, 2, 3]
        )

    def test_attributes(self):
        """
        Test that the attributes of the Place instance are correctly set.
        """
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.user_id, "user123")
        self.assertEqual(self.place.name, "Example Place")
        self.assertEqual(self.place.description, "A cozy place for vacation")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100.00)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, [1, 2, 3])

    def test_default_values(self):
        """
        Test that default values are correctly set when no arguments are pased
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
