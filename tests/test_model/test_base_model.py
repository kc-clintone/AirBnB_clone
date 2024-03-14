#!/usr/bin/python3
"""
Testing the BaseModel module
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Test cases for the base model"""

    def save(self):
        """testing the save method"""
        new_model = BaseModel()
        changes = new_model.updated_at
        write_changes = new_model.save()
        self.assertNotEqual(changes, write_changes)

    def init(self):
    """testing initializing method"""
