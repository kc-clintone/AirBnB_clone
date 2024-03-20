#!/usr/bin/python3
"""
Module for City unittest
"""
from time import sleep
from models.city import City
from datetime import datetime
import os, models, unittest


class TestCity_instantiation(unittest.TestCase):
    """
    Unit testing the instantiation of the City class
    """

    def test_instantiations_with_no_args(self):
        self.assertEqual(City, type(City()))

    def test_instance_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_if_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_if_created_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_if_updated_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_if_state_id_is_a_public_class_attr(self):
        test_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(test_city))
        self.assertNotIn("state_id", test_city.__dict__)

    def test_if_name_is_a_public_class_attr(self):
        c = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(c))
        self.assertNotIn("name", c.__dict__)

    def test_if_two_cities_have_unique_ids(self):
        x = City()
        y = City()
        self.assertNotEqual(x.id, y.id)

    def test_if_two_cities_have_different_created_at(self):
        x = City()
        sleep(0.05)
        y = City()
        self.assertLess(x.created_at, y.created_at)

    def test_if_two_cities_have_different_updated_at(self):
        x = City()
        sleep(0.05)
        y = City()
        self.assertLess(x.updated_at, y.updated_at)

    def test_for_str_repr(self):
        test_date = datetime.today()
        test_date_repr = repr(test_date)
        x = City()
        x.id = "123123"
        x.created_at = x.updated_at = test_date
        xstr = x.__str__()
        self.assertIn("[City] (123123)", xstr)
        self.assertIn("'id': '123123'", xstr)
        self.assertIn("'created_at': " + test_date_repr, xstr)
        self.assertIn("'updated_at': " + test_date_repr, xstr)

    def test_for_unused_args(self):
        test_city = City(None)
        self.assertNotIn(None, test_city.__dict__.values())

    def test_object_instantiation_with_kwargs(self):
        test_date = datetime.today()
        test_date_iso = test_date.isoformat()
        test_city = City(id="123", created_at = test_date_iso, updated_at = test_date_iso)
        self.assertEqual(test_city.id, "123")
        self.assertEqual(test_city.created_at, test_date)
        self.assertEqual(test_city.updated_at, test_date)

    def test_object_instantiation_using_the_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """
    Unit testing the save method of the City class
    """

    @classmethod
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

    def test_one_with_save(self):
        test_subject = City()
        sleep(0.05)
        initial_update = test_subject.updated_at
        test_subject.save()
        self.assertLess(initial_update, test_subject.updated_at)

    def test_two_with_save(self):
        test_subject = City()
        sleep(0.05)
        initial_update = test_subject.updated_at
        test_subject.save()
        subsequent_update = test_subject.updated_at
        self.assertLess(initial_update, subsequent_update)
        sleep(0.05)
        test_subject.save()
        self.assertLess(subsequent_update, test_subject.updated_at)

    def test_for_save_with_args(self):
        x = City()
        with self.assertRaises(TypeError):
            x.save(None)

    def test_if_save_updates_file(self):
        x = City()
        x.save()
        xid = "City." + x.id
        with open("file.json", "r") as f:
            self.assertIn(xid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unit testing for to_dict method for City"""

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

    def test_the_type_for_to_dict(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_if_to_dict_has_valid_keys(self):
        x = City()
        self.assertIn("id", x.to_dict())
        self.assertIn("created_at", x.to_dict())
        self.assertIn("updated_at", x.to_dict())
        self.assertIn("__class__", x.to_dict())

    def test_if_to_dict_has_extra_attr(self):
        x = City()
        x.last_name = "xtremeart"
        x.identification = 254
        self.assertEqual("xtremeart", x.last_name)
        self.assertIn("identification", x.to_dict())

    def test_if_to_dict_datetime_attr_are_strs(self):
        x = City()
        test_dict = x.to_dict()
        self.assertEqual(str, type(test_dict["id"]))
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test_dict["updated_at"]))

    def test_the_output_of_to_dict(self):
        test_date = datetime.today()
        x = City()
        x.id = "12344"
        x.created_at = x.updated_at = test_date
        to_dict = {
            'id': '12344',
            '__class__': 'City',
            'created_at': test_date.isoformat(),
            'updated_at': test_date.isoformat(),
        }
        self.assertDictEqual(x.to_dict(), to_dict)

    def test_for_dunder_dict(self):
        test_subject = City()
        self.assertNotEqual(test_subject.to_dict(),
        test_subject.__dict__)

    def test_the_to_dict_with_arg(self):
        test_subject = City()
        with self.assertRaises(TypeError):
            test_subject.to_dict(None)

if __name__ == "__main__":
    unittest.main()
