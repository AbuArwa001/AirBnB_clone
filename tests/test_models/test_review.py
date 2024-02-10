import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review(
            place_id="123",
            user_id="user456",
            text="This is a great place!"
        )

    def test_attributes(self):
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "user456")
        self.assertEqual(self.review.text, "This is a great place!")

    def test_default_values(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_optional_values(self):
        review = Review(place_id="456")
        self.assertEqual(review.place_id, "456")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

        review = Review(user_id="user789")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "user789")
        self.assertEqual(review.text, "")

        review = Review(text="Another review text")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "Another review text")


if __name__ == '__main__':
    unittest.main()
