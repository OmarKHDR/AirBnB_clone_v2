#!/usr/bin/python3
"""TestState module"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """teststate class"""

    def test_create_instance(self):
        """Test the creation of a State instance"""
        my_state = State()
        self.assertIsNotNone(my_state.id)
        self.assertIsInstance(my_state.created_at, datetime)
        self.assertIsInstance(my_state.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation method"""
        my_state = State()
        self.assertIn("State", str(my_state))

    def test_save_method(self):
        """Test the save method"""
        my_state = State()
        old_updated_at = my_state.updated_at
        my_state.save()
        self.assertNotEqual(old_updated_at, my_state.updated_at)

    def test_update_method(self):
        """Test the update method"""
        my_state = State()
        my_state.update(name="California")
        self.assertEqual(my_state.name, "California")


if __name__ == "__main__":
    unittest.main()

