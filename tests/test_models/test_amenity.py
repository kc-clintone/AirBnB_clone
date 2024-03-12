#!/usr/bin/python3
"""Unittest for amenity class"""

import unittest, time, re, json, os
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Tests for amenity class"""

    def set_up(self):
        """Setting up methods"""
        pass

    def set_off(self):
        """Clears methods."""
        self.resetStorage()
        pass

    def clear_torage(self):
        """Clears FileStorage contents"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests amenity obhect instantiation"""

        base = Amenity()
        self.assertEqual(str(type(base)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(base, Amenity)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_attributes(self):
        """Tests amenity class attributes"""
        attr = storage.attributes()["Amenity"]
        object = Amenity()
        for key, value in attributes.items():
            self.assertTrue(hasattr(object, key))
            self.assertEqual(type(getattr(object, key, None)), value)


if __name__ == "__main__":
    unittest.main()
