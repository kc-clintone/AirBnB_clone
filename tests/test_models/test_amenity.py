#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import models
import unittest
import os
from time import sleep
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """
    Unittests for instantiation of the Amenity class
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

    def test_instances_with_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_if_id_is_public_string(self):
        self.assertEqual(str, type(Amenity().id))

    def test_if_created_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_if_updated_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_if_name_is_a_public_class_attr(self):
        test_amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", test_amenity.__dict__)

    def test_if_two_amenities_possessyunique_ids(self):
        test_amenity_1 = Amenity()
        test_amenity_2 = Amenity()
        self.assertNotEqual(test_amenity_1.id, test_amenity_2.id)

    def test_if_two_amenities_have_different_created_at(self):
        test_amenity_1 = Amenity()
        sleep(0.05)
        test_amenity_2 = Amenity()
        self.assertLess(test_amenity_1.created_at, test_amenity_2.created_at)

    def test_if_two_amenities_have_different_updated_at(self):
        test_amenity_1 = Amenity()
        sleep(0.05)
        test_amenity_2 = Amenity()
        self.assertLess(test_amenity_1.updated_at, test_amenity_2.updated_at)

    def test_for_str_representation(self):
        test_date = datetime.today()
        test_date_repr = repr(test_date)
        test_amenity = Amenity()
        test_amenity.id = "12344"
        test_amenity.created_at = test_amenity.updated_at = test_date
        test_str = test_amenity.__str__()
        self.assertIn("[Amenity] (12344)", test_str)
        self.assertIn("'id': '12344'", test_str)
        self.assertIn("'created_at': " + test_date_repr, test_str)
        self.assertIn("'updated_at': " + test_date_repr, test_str)

    def test_for_unused_args(self):
        test_amenity = Amenity(None)
        self.assertNotIn(None, test_amenity.__dict__.values())

    def test_object_instantiation_with_kwargs(self):
        """
        object instantiation with kwargs
        """
        test_date = datetime.today()
        test_date_iso = test_date.isoformat()
        test_amenity = Amenity(id="254", created_at = test_date_iso, updated_at = test_date_iso)
        self.assertEqual(test_amenity.id, "254")
        self.assertEqual(test_amenity.created_at, test_date)
        self.assertEqual(test_amenity.updated_at, test_date)

    def test_object_instantiation_with_the_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

class TestAmenity_save(unittest.TestCase):
    """
    Unittests for the saving func for the Amenity class
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

    def test_one_with_save(self):
        test_subject = Amenity()
        sleep(0.05)
        initial_update = test_subject.updated_at
        test_subject.save()
        self.assertLess(initial_update, test_subject.updated_at)

    def test_two_with_save(self):
        test_subject = Amenity()
        sleep(0.05)
        initial_update = test_subject.updated_at
        test_subject.save()
        subsequent_update = test_subject.updated_at
        self.assertLess(initial_update, subsequent_update)
        sleep(0.05)
        test_subject.save()
        self.assertLess(subsequent_update, test_subject.updated_at)

    def test_for_save_with_arg(self):
        x = Amenity()
        with self.assertRaises(TypeError):
            x.save(None)

    def test_save_updates_file(self):
        x = Amenity()
        x.save()
        xid = "Amenity." + x.id
        with open("file.json", "r") as f:
            self.assertIn(xid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """
    Unit testing the to_dict method for Amenity
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

    def test_the_type_for_to_dict(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_if_to_dict_has_valid_keys(self):
        x = Amenity()
        self.assertIn("id", x.to_dict())
        self.assertIn("created_at", x.to_dict())
        self.assertIn("updated_at", x.to_dict())
        self.assertIn("__class__", x.to_dict())

    def test_if_to_dict_has_extra_attr(self):
        x = Amenity()
        x.last_name = "xtremeart"
        x.identification = 254
        self.assertEqual("xtremeart", x.last_name)
        self.assertIn("identification", x.to_dict())

    def test_if_to_dict_datetime_attr_are_strs(self):
        x = Amenity()
        test_dict = x.to_dict()
        self.assertEqual(str, type(test_dict["id"]))
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test_dict["updated_at"]))

    def test_the_output_of_to_dict(self):
        test_date = datetime.today()
        x = Amenity()
        x.id = "12344"
        x.created_at = x.updated_at = test_date
        to_dict = {
            'id': '12344',
            '__class__': 'Amenity',
            'created_at': test_date.isoformat(),
            'updated_at': test_date.isoformat(),
        }
        self.assertDictEqual(x.to_dict(), to_dict)

    def test_for_dunder_dict(self):
        test_subject = Amenity()
        self.assertNotEqual(test_subject.to_dict(), test_subject.__dict__)

    def test_the_to_dict_with_arg(self):
        test_subject = Amenity()
        with self.assertRaises(TypeError):
            test_subject.to_dict(None)


if __name__ == "__main__":
    unittest.main()
