#!/usr/bin/python3
"""TestReview module"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """testreview class"""

    def test_create_instance(self):
        """Test the creation of a Review instance"""
        my_review = Review()
        self.assertIsNotNone(my_review.id)
        self.assertIsInstance(my_review.created_at, datetime)
        self.assertIsInstance(my_review.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation method"""
        my_review = Review()
        self.assertIn("Review", str(my_review))

    def test_save_method(self):
        """Test the save method"""
        my_review = Review()
        old_updated_at = my_review.updated_at
        my_review.save()
        self.assertNotEqual(old_updated_at, my_review.updated_at)

    def test_update_method(self):
        """Test the update method"""
        my_review = Review()
        my_review.update(text="Great place!")
        self.assertEqual(my_review.text, "Great place!")


if __name__ == "__main__":
    unittest.main()

