#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
import sys
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.state import State
from models.place import Place

class TestConsole(unittest.TestCase):
	"""Test the console"""

	def setUp(self):
		"""Set up the console for testing"""
		self.console = HBNBCommand()
		sys.stdout = StringIO()

	def tearDown(self):
		"""Clean up after testing"""
		sys.stdout = sys.__stdout__

	def test_create_with_params(self):
		"""Test create command with parameters"""
		self.console.onecmd("create State name=\"California\"")
		self.assertIn("State", self.console.stdout.getvalue())
		state_id = self.console.stdout.getvalue().split()[1].strip()
		self.assertTrue(uuid.UUID(state_id, version=4))

if __name__ == "__main__":
	unittest.main()
