import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State(name="California")

    def test_attributes(self):
        self.assertEqual(self.state.name, "California")

    def test_default_values(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_optional_name(self):
        state = State()
        self.assertEqual(state.name, "")

        state = State(name="New York")
        self.assertEqual(state.name, "New York")


if __name__ == '__main__':
    unittest.main()
