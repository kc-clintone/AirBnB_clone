#!/usr/bin/python3
"""Unittest for City"""

import unittest, os, time, re, json
from models import storage
from models.city import City
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """Tests for City"""

    def set_up(self):
        """Sets up methods"""
        pass

    def set_off(self):
        """Resets methods."""
        self.resetStorage()
        pass

    def clear_storage(self):
        """Clears FileStorage content"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of City class."""

        base = City()
        self.assertEqual(str(type(base)), "<class 'models.city.City'>")
        self.assertIsInstance(base, City)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_attributes(self):
        """Tests attributes for City"""
        attr = storage.attributes()["City"]
        object = City()
        for key, value in attributes.items():
            self.assertTrue(hasattr(object, key))
            self.assertEqual(type(getattr(object, key, None)), value)


if __name__ == "__main__":
    unittest.main()
