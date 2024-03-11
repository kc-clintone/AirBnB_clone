#!/usr/bin/python3
"""In this module we write unittest for BaseModel Class"""

#from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json, os, re, time, unittest, uuid


class TestBaseModel(unittest.TestCase):

    """The following arw test cases for BaseModel"""

    def clear_storage(self):
        """Resetting the local storage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def set_up(self):
        """Setting up the test methods"""
        pass

    def set_off(self):
        """Setting off the test methods"""
        self.resetStorage()
        pass

    def instantiating(self):
        """Testing instantiation of the BaseModel"""

        base = BaseModel()
        self.assertEqual(str(type(base)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_no_args(self):
        """Testing the __init__ file without any args"""
        self.resetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.__init__()
        err_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), err_msg)

    def test_many_args(self):
        """Testing the __init__ filebwith many args."""
        self.resetStorage()
        args = [i for i in range(1000)]
        bse = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        bse = BaseModel(*args)

    def test_attributes(self):
        """Testing the attribute values for instances of the BaseModel"""

        attr = storage.attributes()["BaseModel"]
        base_class = BaseModel()
        for k, v in attr.items():
            self.assertTrue(hasattr(base_class, k))
            self.assertEqual(type(getattr(base_class, k, None)), v)

    def test_time_created(self):
        """Testing updated_at & createf_at during creation"""
        today = datetime.now()
        base = BaseModel()
        td = base.updated_at - b.created_at
        self.assertTrue(abs(td.total_seconds()) < 0.01)
        td = base.created_at - date_now
        self.assertTrue(abs(td.total_seconds()) < 0.1)

    def test_id(self):
        """Testing the uuid"""

        bs = [BaseModel().id for k in range(1000)]
        self.assertEqual(len(set(bs)), len(bs))

    def test_save(self):
        """Testing method save()"""

        base = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        base.save()
        td = base.updated_at - date_now
        self.assertTrue(abs(td.total_seconds()) < 0.01)

    def test_str(self):
        """Testing the __str__ method"""
        base = BaseModel()
        regex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        response = regex.match(str(base))
        self.assertIsNotNone(response)
        self.assertEqual(response.group(1), "BaseModel")
        self.assertEqual(response.group(2), base.id)
        str = response.group(3)
        str = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", str)
        dlt = json.loads(str.replace("'", '"'))
        dlts = base.__dict__.copy()
        dlts["created_at"] = repr(dlts["created_at"])
        dlts["updated_at"] = repr(dlts["updated_at"])
        self.assertEqual(dlt, dlts)

    def test_to_dict(self):
        """Testing the method to_dict()"""

        base = BaseModel()
        base.name = "Laura"
        base.age = 23
        x = base.to_dict()
        self.assertEqual(x["id"], base.id)
        self.assertEqual(x["__class__"], type(base).__name__)
        self.assertEqual(x["created_at"], base.created_at.isoformat())
        self.assertEqual(x["updated_at"], base.updated_at.isoformat())
        self.assertEqual(x["name"], base.name)
        self.assertEqual(x["age"], base.age)

    def test_to_dict_no_args(self):
        """Testing to_dict() with no args"""
        self.resetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.to_dict()
        err_msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), err_msg)

    def test_to_dict_excess_args(self):
        """Testing to_dict() with many args"""
        self.resetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.to_dict(self, 98)
        err_msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(err.exception), err_msg)

    def test_instantiation(self):
        """Testing the instantiation with **kwargs"""

        new_model = BaseModel()
        new_model.name = "Holberton"
        new_model.new_number = 89
        new_model_json = new_model.to_dict()
        new_new_model = BaseModel(**new_model_json)
        self.assertEqual(new_new_model.to_dict(), new_model.to_dict())

    def test_instantiation_dict(self):
        """Testing the instantiation with **kwargs dict"""
        x = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        out = BaseModel(**x)
        self.assertEqual(out.to_dict(), x)

    def testing_save(self):
        """Testing the storage.save(), called from save()"""
        self.resetStorage()
        base = BaseModel()
        base.save()
        k = "{}.{}".format(type(base).__name__, base.id)
        x = {k: base.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(x)))
            f.seek(0)
            self.assertEqual(json.load(f), x)

    def test_save_no_args(self):
        """Testing the save() with no args"""
        self.resetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.save()
        err_msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), err_msg)

    def test_save_excess_args(self):
        """Testing save() with many args"""
        self.resetStorage()
        with self.assertRaises(TypeError) as err:
            BaseModel.save(self, 98)
        err_msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), err_msg)


if __name__ == '__main__':
    unittest.main()
