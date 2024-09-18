#!/usr/bin/python3
"""TestPlace module"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """testplace class"""

    def test_create_instance(self):
        """Test the creation of a Place instance"""
        my_place = Place()
        self.assertIsNotNone(my_place.id)
        self.assertIsInstance(my_place.created_at, datetime)
        self.assertIsInstance(my_place.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation method"""
        my_place = Place()
        self.assertIn("Place", str(my_place))

    def test_save_method(self):
        """Test the save method"""
        my_place = Place()
        old_updated_at = my_place.updated_at
        my_place.save()
        self.assertNotEqual(old_updated_at, my_place.updated_at)

    def test_update_method(self):
        """Test the update method"""
        my_place = Place()
        my_place.update(name="Cozy Apartment")
        self.assertEqual(my_place.name, "Cozy Apartment")


if __name__ == "__main__":
    unittest.main()

