#!/usr/bin/python3
"""TestAmenity module"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """test amenity class"""

    def test_create_instance(self):
        """Test the creation of an Amenity instance"""
        my_amenity = Amenity()
        self.assertIsNotNone(my_amenity.id)
        self.assertIsInstance(my_amenity.created_at, datetime)
        self.assertIsInstance(my_amenity.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation method"""
        my_amenity = Amenity()
        self.assertIn("Amenity", str(my_amenity))

    def test_save_method(self):
        """Test the save method"""
        my_amenity = Amenity()
        old_updated_at = my_amenity.updated_at
        my_amenity.save()
        self.assertNotEqual(old_updated_at, my_amenity.updated_at)

    def test_update_method(self):
        """Test the update method"""
        my_amenity = Amenity()
        my_amenity.update(name="WiFi")
        self.assertEqual(my_amenity.name, "WiFi")


if __name__ == "__main__":
    unittest.main()

