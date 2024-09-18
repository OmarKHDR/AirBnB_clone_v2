#!/usr/bin/python3
"""TESTBASE module"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        """Test the creation of a BaseModel instance"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation method"""
        my_model = BaseModel()
        self.assertIn("BaseModel", str(my_model))

    def test_save_method(self):
        """Test the save method"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("__class__", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)

if __name__ == "__main__":
    unittest.main()

