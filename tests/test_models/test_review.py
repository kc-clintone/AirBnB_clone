#!/usr/bin/python3
"""Unittest for Reviews"""

import unittest, os, time, re, json
from models import storage
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestReview(unittest.TestCase):
    """Tests for Review"""

    def set_up(self):
        """Sets methods"""
        pass

    def set_off(self):
        """Clears methods"""
        self.resetStorage()
        pass

    def clear_storage(self):
        """Clears FileStorage content"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests Review object instantiation"""

        base = Review()
        self.assertEqual(str(type(base)), "<class 'models.review.Review'>")
        self.assertIsInstance(base, Review)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_attributes(self):
        """Tests attributes Review"""
        attr = storage.attributes()["Review"]
        object = Review()
        for key, value in attributes.items():
            self.assertTrue(hasattr(object, key))
            self.assertEqual(type(getattr(object, key, None)), value)


if __name__ == "__main__":
    unittest.main()
