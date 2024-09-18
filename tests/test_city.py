#!/usr/bin/python3
"""TestCity module"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """testcity class"""

    def test_create_instance(self):
        """Test the creation of a City instance"""
        my_city = City()
        self.assertIsNotNone(my_city.id)
        self.assertIsInstance(my_city.created_at, datetime)
        self.assertIsInstance(my_city.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation method"""
        my_city = City()
        self.assertIn("City", str(my_city))

    def test_save_method(self):
        """Test the save method"""
        my_city = City()
        old_updated_at = my_city.updated_at
        my_city.save()
        self.assertNotEqual(old_updated_at, my_city.updated_at)

    def test_update_method(self):
        """Test the update method"""
        my_city = City()
        my_city.update(name="New York")
        self.assertEqual(my_city.name, "New York")


if __name__ == "__main__":
    unittest.main()

