#!/usr/bin/python3
"""
FilStorage unittest module
"""
import os, json, models, unittest
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for instantiation of filestorage
    """
    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for  methods of the FileStorage class
    """
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        test_model = BaseModel()
        test_user = User()
        test_state = State()
        test_place = Place()
        test_city = City()
        test_amenity = Amenity()
        test_review = Review()
        models.storage.new(test_model)
        models.storage.new(test_user)
        models.storage.new(test_state)
        models.storage.new(test_place)
        models.storage.new(test_city)
        models.storage.new(test_amenity)
        models.storage.new(test_review)
        self.assertIn("BaseModel." + test_model.id, models.storage.all().keys())
        self.assertIn(test_model, models.storage.all().values())
        self.assertIn("User." + test_user.id, models.storage.all().keys())
        self.assertIn(test_user, models.storage.all().values())
        self.assertIn("State." + test_state.id, models.storage.all().keys())
        self.assertIn(test_state, models.storage.all().values())
        self.assertIn("Place." + test_place.id, models.storage.all().keys())
        self.assertIn(test_place, models.storage.all().values())
        self.assertIn("City." + test_city.id, models.storage.all().keys())
        self.assertIn(test_city, models.storage.all().values())
        self.assertIn("Amenity." + test_amenity.id, models.storage.all().keys())
        self.assertIn(test_amenity, models.storage.all().values())
        self.assertIn("Review." + test_review.id, models.storage.all().keys())
        self.assertIn(test_review, models.storage.all().values())

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_save(self):
        test_model = BaseModel()
        test_user = User()
        test_state = State()
        test_place = Place()
        test_city = City()
        test_amenity = Amenity()
        test_review = Review()
        models.storage.new(test_model)
        models.storage.new(test_user)
        models.storage.new(test_state)
        models.storage.new(test_place)
        models.storage.new(test_city)
        models.storage.new(test_amenity)
        models.storage.new(test_review)
        models.storage.save()
        buffer = ""
        with open("file.json", "r") as f:
            buffer = f.read()
            self.assertIn("BaseModel." + test_model.id, buffer)
            self.assertIn("User." + test_user.id, buffer)
            self.assertIn("State." + test_state.id, buffer)
            self.assertIn("Place." + test_place.id, buffer)
            self.assertIn("City." + test_city.id, buffer)
            self.assertIn("Amenity." + test_amenity.id, buffer)
            self.assertIn("Review." + test_review.id, buffer)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload(self):
        test_model = BaseModel()
        test_user = User()
        test_state = State()
        test_place = Place()
        test_city = City()
        test_amenity = Amenity()
        test_review = Review()
        models.storage.new(test_model)
        models.storage.new(test_user)
        models.storage.new(test_state)
        models.storage.new(test_place)
        models.storage.new(test_city)
        models.storage.new(test_amenity)
        models.storage.new(test_review)
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + test_model.id, objects)
        self.assertIn("User." + test_user.id, objects)
        self.assertIn("State." + test_state.id, objects)
        self.assertIn("Place." + test_place.id, objects)
        self.assertIn("City." + test_city.id, objects)
        self.assertIn("Amenity." + test_amenity.id, objects)
        self.assertIn("Review." + test_review.id, objects)


if __name__ == "__main__":
    unittest.main()
