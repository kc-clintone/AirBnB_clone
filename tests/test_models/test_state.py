#!/usr/bin/python3
"""Unittest for States"""

import unittest, os, time, re, json
from models import storage
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestState(unittest.TestCase):
    """Tests for State"""

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
        """Tests State object instantiation"""

        base = State()
        self.assertEqual(str(type(base)), "<class 'models.state.State'>")
        self.assertIsInstance(base, State)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_attributes(self):
        """Tests attributes State"""
        attr = storage.attributes()["State"]
        object = State()
        for key, value in attributes.items():
            self.assertTrue(hasattr(object, key))
            self.assertEqual(type(getattr(object, key, None)), value)


if __name__ == "__main__":
    unittest.main()
