"""
Module to test the functionality of the State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up a test instance of the State class.
        """
        self.state = State(name="California")

    def test_attributes(self):
        """
        Test that the attributes of the State instance are correctly set.
        """
        self.assertEqual(self.state.name, "California")

    def test_default_values(self):
        """
        Test that default values are correctly set when no arguments are passd
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_optional_name(self):
        """
        Test that an optional name argument can be passed correctly.
        """
        # Test with no arguments
        state = State()
        self.assertEqual(state.name, "")

        # Test with name argument
        state = State(name="New York")
        self.assertEqual(state.name, "New York")


if __name__ == "__main__":
    unittest.main()
