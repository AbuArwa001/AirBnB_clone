"""
Module to test the functionality of the User class.
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up a default user instance and a custom user instance for testing.
        """
        self.default_user = User()
        self.custom_user = User(
            email="test@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )

    def test_attributes_initialization(self):
        """
        Test that attributes are correctly initialized when passing arguments.
        """
        user = self.custom_user
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_attributes_default_values(self):
        """
        Test that default values are correctly set
        when no arguments are passed.
        """
        user = self.default_user
        self.assertNotIn("email", user.__dict__)
        self.assertNotIn("password", user.__dict__)
        self.assertNotIn("first_name", user.__dict__)
        self.assertNotIn("last_name", user.__dict__)

    def test_inheritance(self):
        """
        Test that User class inherits from BaseModel class.
        """
        user = self.default_user
        self.assertTrue(isinstance(user, BaseModel))

    def test_initialization_with_args(self):
        """
        Test that User can be initialized with arguments directly.
        """
        user = User("test@example.com", "password", "John", "Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_initialization_with_kwargs(self):
        """
        Test that User can be initialized with keyword arguments.
        """
        user = self.custom_user
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
