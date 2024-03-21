#!/usr/bin/python3
"""
Module for State
"""
import os, models, unittest
from datetime import datetime
from time import sleep
from models.user import State


class TestState_instantiation(unittest.TestCase):
    """
    Unit testing the instantiation of the State class
    """

    def test_no_args_instances(self):
        self.assertEqual(State, type(State()))

    def test_for_new_instances_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_if_the_id_is_a_public_string(self):
        self.assertEqual(str, type(State().id))

    def test_if_the_created_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_if_the_updated_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_if_two_states_have_unique_ids(self):
        test_state_1 = State()
        test_state_2 = State()
        self.assertNotEqual(test_state_1.id, test_state_2.id)

    def test_if_two_state_have_different_created_at(self):
        test_Slstate_1 = State()
        sleep(0.05)
        test_state_2 = State()
        self.assertLess(test_state_1.created_at, test_state_2.created_at)

    def test_if_name_is_a_public_class_attr(self):
        x = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(x))
        self.assertNotIn("name", x.__dict__)

    def test_if_two_state_have_different_updated_at(self):
        test_state_1 = State()
        sleep(0.05)
        test_state_2 = State()
        self.assertLess(test_state_1.updated_at, test_state_2.updated_at)

    def test_the_str_repr(self):
        test_date = datetime.today()
        test_date_repr = repr(test_date)
        test_state = State()
        test_state.id = "12344"
        test_state.created_at = test_state.updated_at = test_date
        state_str = test_state.__str__()
        self.assertIn("[State] (12344)", state_str)
        self.assertIn("'id': '12344'", state_str)
        self.assertIn("'created_at': " + test_date_repr, state_str)
        self.assertIn("'updated_at': " + test_date_repr, state_str)

    def test_for_unused_args(self):
        test_state = State(None)
        self.assertNotIn(None, test_state.__dict__.values())

    def test_object_instantiation_with_kwargs(self):
        x = datetime.today()
        xiso = x.isoformat()
        test_state = State(id="254", created_at = xiso, updated_at = xiso)
        self.assertEqual(test_state.id, "254")
        self.assertEqual(test_state.created_at, x)
        self.assertEqual(test_state.updated_at, x)

    def test_object_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
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
        x = State()
        sleep(0.05)
        initial_update = x.updated_at
        x.save()
        self.assertLess(initial_update, x.updated_at)

    def test_two_with_save(self):
        x = State()
        sleep(0.05)
        initial_update = x.updated_at
        x.save()
        subsequent_update = x.updated_at
        self.assertLess(initial_update, subsequent_update)
        sleep(0.05)
        x.save()
        self.assertLess(subsequent_update, test_usr.updated_at)

    def test_save_with_args(self):
        x = State()
        with self.assertRaises(TypeError):
            x.save(None)

    def test_if_save_updates_file(self):
        x = State()
        x.save()
        xid = "State." + x.id
        with open("file.json", "r") as f:
            self.assertIn(xid, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State"""

    def test_type_of_to_dict(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_if_to_dict_has_valid_keys(self):
        x = State()
        self.assertIn("id", x.to_dict())
        self.assertIn("created_at", x.to_dict())
        self.assertIn("updated_at", x.to_dict())
        self.assertIn("__class__", x.to_dict())

    def test_if_to_dict_has_extra_attr(self):
        x = State()
        x.last_name = "Nairobi"
        x.identification = 989
        self.assertEqual("Nairobi", x.last_name)
        self.assertIn("identification", x.to_dict())

    def test_if_to_dict_datetime_attrs_are_strings(self):
        x = State()
        state_dict = x.to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def test_output_of_to_dict(self):
        test_date = datetime.today()
        test_state = State()
        test_state.id = "12344"
        test_state.created_at = test_state.updated_at = test_date
        todict = {
            'id': '12344',
            '__class__': 'State',
            'created_at': test_date.isoformat(),
            'updated_at': test_date.isoformat(),
        }
        self.assertDictEqual(test_state.to_dict(), todict)

    def test_dunder_dict(self):
        ste = State()
        self.assertNotEqual(ste.to_dict(), ste.__dict__)

    def test_the_to_dict_with_arg(self):
        x = State()
        with self.assertRaises(TypeError):
            x.to_dict(None)


if __name__ == "__main__":
    unittest.main()
