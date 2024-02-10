import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City(state_id="CA", name="San Francisco")

    def test_attributes(self):
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_default_values(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_optional_values(self):
        city = City(state_id="NY")
        self.assertEqual(city.state_id, "NY")
        self.assertEqual(city.name, "")

        city = City(name="Los Angeles")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "Los Angeles")

        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
