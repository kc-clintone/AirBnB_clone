#!/usr/bin/python3
"""
Module for User class
"""
import os, models, unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """
    Unit testing the instantiation of the User class
    """

    def test_no_args_instances(self):
        self.assertEqual(User, type(User()))

    def test_for_new_instances_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_if_the_id_is_a_public_string(self):
        self.assertEqual(str, type(User().id))

    def test_if_the_created_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_if_the_updated_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_if_the_email_is_a_public_string(self):
        self.assertEqual(str, type(User.email))

    def test_if_the_password_is_a_public_string(self):
        self.assertEqual(str, type(User.password))

    def test_if_first_name_is_a_public_string(self):
        self.assertEqual(str, type(User.first_name))

    def test_if_last_name_is_a_public_string(self):
        self.assertEqual(str, type(User.last_name))

    def test_if_two_users_have_unique_ids(self):
        test_user_1 = User()
        test_user_2 = User()
        self.assertNotEqual(test_user_1.id, test_user_2.id)

    def test_if_two_users_have_different_created_at(self):
        test_user_1 = User()
        sleep(0.05)
        test_user_2 = User()
        self.assertLess(test_user_1.created_at, test_user_2.created_at)

    def test_if_two_users_have_different_updated_at(self):
        test_user_1 = User()
        sleep(0.05)
        test_user_2 = User()
        self.assertLess(test_user_1.updated_at, test_user_2.updated_at)

    def test_the_str_repr(self):
        test_date = datetime.today()
        test_date_repr = repr(test_date)
        test_user = User()
        test_user.id = "12344"
        test_user.created_at = test_user.updated_at = test_date
        u_str = test_user.__str__()
        self.assertIn("[User] (12344)", u_str)
        self.assertIn("'id': '12344'", u_str)
        self.assertIn("'created_at': " + test_date_repr, u_str)
        self.assertIn("'updated_at': " + test_date_repr, u_str)

    def test_for_unused_args(self):
        test_user = User(None)
        self.assertNotIn(None, test_user.__dict__.values())

    def test_objext_instantiation_with_kwargs(self):
        x = datetime.today()
        xiso = x.isoformat()
        test_user = User(id="254", created_at = xiso, updated_at = xiso)
        self.assertEqual(test_user.id, "254")
        self.assertEqual(test_user.created_at, x)
        self.assertEqual(test_user.updated_at, x)

    def test_object_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_with_save(self):
        test_usr = User()
        sleep(0.05)
        initial_update = test_usr.updated_at
        test_usr.save()
        self.assertLess(initial_update, test_usr.updated_at)

    def test_two_with_save(self):
        test_usr = User()
        sleep(0.05)
        initial_update = test_usr.updated_at
        test_usr.save()
        subsequent_update = test_usr.updated_at
        self.assertLess(initial_update, subsequent_update)
        sleep(0.05)
        test_usr.save()
        self.assertLess(subsequent_update, test_usr.updated_at)

    def test_save_with_args(self):
        test_usr = User()
        with self.assertRaises(TypeError):
            test_usr.save(None)

    def test_if_save_updates_file(self):
        test_usr = User()
        test_usr.save()
        usrid = "User." + test_usr.id
        with open("file.json", "r") as f:
            self.assertIn(usrid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_type_of_to_dict(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_if_to_dict_has_valid_keys(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_if_to_dict_has_extra_attr(self):
        usr = User()
        usr.last_name = "kaysee"
        usr.identification = 20
        self.assertEqual("kaysee", usr.last_name)
        self.assertIn("identification", usr.to_dict())

    def test_if_to_dict_datetime_attrs_are_strings(self):
        usr = User()
        usrdict = usr.to_dict()
        self.assertEqual(str, type(usrdict["id"]))
        self.assertEqual(str, type(usrdict["created_at"]))
        self.assertEqual(str, type(usrdict["updated_at"]))

    def test_output_of_to_dict(self):
        test_date = datetime.today()
        usr = User()
        usr.id = "12344"
        usr.created_at = usr.updated_at = test_date
        todict = {
            'id': '12344',
            '__class__': 'User',
            'created_at': test_date.isoformat(),
            'updated_at': test_date.isoformat(),
        }
        self.assertDictEqual(usr.to_dict(), todict)

    def test_dunder_dict(self):
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def test_the_to_dict_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()
