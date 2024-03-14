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
        save_changes = new_model.save()
        self.assertNotEqual(changes, save_changes)

    def init(self):
    """testing initializing method"""
        test_model = BaseModel()
        self.assertIsNotNone(test_model.id)
        self.assertIsNotNone(test_model.created_at)
        self.assertIsNotNone(test_model.updated_at)

    def to_dict(self):
    """testing dictionary method"""
        test_model = BaseModel()
        test_dict = test_model.to_dict()
        self.assertIsInstance(test_dict, dict)

        self.assertEqual(test_dict["__class__"], "BaseModel")
        self.assertEqual(test_dict["id"], test_model.id)
        self.assertEqual(test_dict["created_at"], test_model.created_at.isoformat())
        self.assertEqual(test_dict["updated_at"], test_model.updated_at.isoformat())

    def test_str(self):
    """testing the string method"""
        new_model = BaseModel()
        self.assertTrue(str(new_model).startswith('[BaseModel]'))
        self.assertIn(new_model.id, str(new_model))
        self.assertIn(str(new_model.__dict__), str(new_model))

if __name__ == "__main__":
    unittest.main()
