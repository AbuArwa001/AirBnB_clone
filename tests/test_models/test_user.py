import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        self.default_user = User()
        self.custom_user = User(
            email="test@example.com", password="password",
            first_name="John", last_name="Doe"
            )

    def test_attributes_initialization(self):
        user = self.custom_user
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_attributes_default_values(self):
        user = self.default_user
        self.assertNotIn('email', user.__dict__)
        self.assertNotIn('password', user.__dict__)
        self.assertNotIn('first_name', user.__dict__)
        self.assertNotIn('last_name', user.__dict__)

    def test_inheritance(self):
        user = self.default_user
        self.assertTrue(isinstance(user, BaseModel))

    def test_initialization_with_args(self):
        user = User("test@example.com", "password", "John", "Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_initialization_with_kwargs(self):
        user = self.custom_user
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
