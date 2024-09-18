#!/usr/bin/python3
"""TestUser module"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """test user class"""

    def test_create_instance(self):
        """Test the creation of a User instance"""
        my_user = User()
        self.assertIsNotNone(my_user.id)
        self.assertIsInstance(my_user.created_at, datetime)
        self.assertIsInstance(my_user.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation method"""
        my_user = User()
        self.assertIn("User", str(my_user))

    def test_save_method(self):
        """Test the save method"""
        my_user = User()
        old_updated_at = my_user.updated_at
        my_user.save()
        self.assertNotEqual(old_updated_at, my_user.updated_at)

    def test_update_method(self):
        """Test the update method"""
        my_user = User()
        my_user.update(email="user@example.com")
        self.assertEqual(my_user.email, "user@example.com")


if __name__ == "__main__":
    unittest.main()

