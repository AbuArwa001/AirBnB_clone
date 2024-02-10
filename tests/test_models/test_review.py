"""
Module to test the functionality of the Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up a test instance of the Review class.
        """
        self.review = Review(
            place_id="123",
            user_id="user456",
            text="This is a great place!"
        )

    def test_attributes(self):
        """
        Test that the attributes of the Review instance are correctly set.
        """
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "user456")
        self.assertEqual(self.review.text, "This is a great place!")

    def test_default_values(self):
        """
        Test that default values are correctly set when no args are passed.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_optional_values(self):
        """
        Test that optional place_id, user_id, and text arguments
        can be passed correctly.
        """
        # Test with place_id only
        review = Review(place_id="456")
        self.assertEqual(review.place_id, "456")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

        # Test with user_id only
        review = Review(user_id="user789")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "user789")
        self.assertEqual(review.text, "")

        # Test with text only
        review = Review(text="Another review text")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "Another review text")


if __name__ == '__main__':
    unittest.main()
