#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Place class.
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

    def test_instantiations_without_args(self):
        self.assertEqual(Place, type(Place()))

    def test_instance_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_if_id_is_a_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_if_created_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_if_the_updated_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_if_the_city_id_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(x))
        self.assertNotIn("city_id", x.__dict__)

    def test_if_the_user_id_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(x))
        self.assertNotIn("user_id", x.__dict__)

    def test_if_name_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(x))
        self.assertNotIn("name", x.__dict__)

    def test_if_the_description_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(x))
        self.assertNotIn("desctiption", x.__dict__)

    def test_if_the_number_rooms_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(x))
        self.assertNotIn("number_rooms", x.__dict__)

    def test_if_the_number_bathrooms_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(x))
        self.assertNotIn("number_bathrooms", x.__dict__)

    def test_if_max_guest_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(x))
        self.assertNotIn("max_guest", x.__dict__)

    def test_if_price_by_night_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(x))
        self.assertNotIn("price_by_night", x.__dict__)

    def test_if_latitude_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(x))
        self.assertNotIn("latitude", x.__dict__)

    def test_if_longitude_is_a_public_class_attribute(self):
        x = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(x))
        self.assertNotIn("longitude", x.__dict__)

    def test_if_the_amenity_ids_are_public_class_attributes(self):
        x = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(x))
        self.assertNotIn("amenity_ids", x.__dict__)

    def test_if_two_places_possess_unique_ids(self):
        test_place_1 = Place()
        test_place_2 = Place()
        self.assertNotEqual(test_place_1.id, test_place_2.id)

    def test_if_two_places_have_different_created_at(self):
        test_place_1 = Place()
        sleep(0.05)
        test_place_2 = Place()
        self.assertLess(test_place_1.created_at, test_place_2.created_at)

    def test_if_two_places_have_different_updated_at(self):
        test_place_1 = Place()
        sleep(0.05)
        test_place_2 = Place()
        self.assertLess(test_place_1.updated_at, test_place_2.updated_at)

    def test_for_str_representation(self):
        test_date = datetime.today()
        test_date_repr = repr(test_date)
        x = Place()
        x.id = "12344"
        x.created_at = x.updated_at = test_date
        test_str = x.__str__()
        self.assertIn("[Place] (12344)", test_str)
        self.assertIn("'id': '12344'", test_str)
        self.assertIn("'created_at': " + test_date_repr, test_str)
        self.assertIn("'updated_at': " + test_date_repr, test_str)

    def test_for_unused_args(self):
        x = Place(None)
        self.assertNotIn(None, x.__dict__.values())

    def test_object_instantiation_with_kwargs(self):
        """
        object instantiation with kwargs
        """
        test_date = datetime.today()
        test_date_iso = test_date.isoformat()
        x = Place(id="254", created_at = test_date_iso, updated_at = test_date_iso)
        self.assertEqual(x.id, "254")
        self.assertEqual(x.created_at, test_date)
        self.assertEqual(x.updated_at, test_date)

    def test_object_instantiation_with_the_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

class TestPlace_save(unittest.TestCase):
    """
    Unittests for testing save method of the Place class.
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
        test_subject = Place()
        sleep(0.05)
        initial_update = test_subject.updated_at
        test_subject.save()
        self.assertLess(initial_update, test_subject.updated_at)

    def test_two_with_save(self):
        test_subject = Place()
        sleep(0.05)
        initial_update = test_subject.updated_at
        test_subject.save()
        subsequent_update = test_subject.updated_at
        self.assertLess(initial_update, subsequent_update)
        sleep(0.05)
        test_subject.save()
        self.assertLess(subsequent_update, test_subject.updated_at)

    def test_for_save_with_arg(self):
        x = Place()
        with self.assertRaises(TypeError):
            x.save(None)

    def test_save_updates_file(self):
        x = Place()
        x.save()
        xid = "Place." + x.id
        with open("file.json", "r") as f:
            self.assertIn(xid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    Unit testing the to_dict method of the Place class
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
        self.assertTrue(dict, type(Place().to_dict()))

    def test_if_to_dict_has_valid_keys(self):
        x = Place()
        self.assertIn("id", x.to_dict())
        self.assertIn("created_at", x.to_dict())
        self.assertIn("updated_at", x.to_dict())
        self.assertIn("__class__", x.to_dict())

    def test_if_to_dict_has_extra_attr(self):
        x = Place()
        x.last_name = "xtremeart"
        x.identification = 254
        self.assertEqual("xtremeart", x.last_name)
        self.assertIn("identification", x.to_dict())

    def test_if_to_dict_datetime_attr_are_strs(self):
        x = Place()
        test_dict = x.to_dict()
        self.assertEqual(str, type(test_dict["id"]))
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test_dict["updated_at"]))

    def test_the_output_of_to_dict(self):
        test_date = datetime.today()
        x = Place()
        x.id = "12344"
        x.created_at = x.updated_at = test_date
        to_dict = {
            'id': '12344',
            '__class__': 'Place',
            'created_at': test_date.isoformat(),
            'updated_at': test_date.isoformat(),
        }
        self.assertDictEqual(x.to_dict(), to_dict)

    def test_for_dunder_dict(self):
        test_subject = Place()
        self.assertNotEqual(test_subject.to_dict(), test_subject.__dict__)

    def test_the_to_dict_with_arg(self):
        test_subject = Place()
        with self.assertRaises(TypeError):
            test_subject.to_dict(None)


if __name__ == "__main__":
    unittest.main()
