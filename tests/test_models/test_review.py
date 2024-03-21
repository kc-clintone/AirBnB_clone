#!/usr/bin/python3
"""
Unit testing Review
"""
import os, models, unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """
    Unit testing instantiation for Review
    """

    def test_instances_with_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_instances_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_if_id_is_a_public_string(self):
        self.assertEqual(str, type(Review().id))

    def test_if_created_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_if_updated_at_is_a_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_if_placeid_is_a_public_class_attribute(self):
        test_review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(test_review))
        self.assertNotIn("place_id", test_review.__dict__)

    def test_if_userid_is_a_public_class_attr(self):
        test_review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(test_review))
        self.assertNotIn("user_id", test_review.__dict__)

    def test_if_text_is_a_public_class_attr(self):
        test_review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(test_review))
        self.assertNotIn("text", test_review.__dict__)

    def test_if_two_reviews_have_unique_ids(self):
        test_review_1 = Review()
        test_review_2 = Review()
        self.assertNotEqual(test_review_1.id, test_review_2.id)

    def test_if_two_reviews_have_different_created_at(self):
        test_review_1 = Review()
        sleep(0.05)
        test_review_2 = Review()
        self.assertLess(test_review_1.created_at, test_review_2.created_at)

    def test_if_two_reviews_have_different_updated_at(self):
        test_review_1 = Review()
        sleep(0.05)
        test_review_2 = Review()
        self.assertLess(test_review_1.updated_at, test_review_2.updated_at)

    def test_for_str_repr(self):
        test_date = datetime.today()
        x = repr(test_date)
        test_review = Review()
        test_review.id = "123123"
        test_review.created_at = test_review.updated_at = test_date
        y = test_review.__str__()
        self.assertIn("[Review] (123123)", y)
        self.assertIn("'id': '123123'", y)
        self.assertIn("'created_at': " + x, y)
        self.assertIn("'updated_at': " + x, y)

    def test_for_unused_args(self):
        x = Review(None)
        self.assertNotIn(None, x.__dict__.values())

    def test_object_instantiation_with_kwargs(self):
        test_date = datetime.today()
        x = test_date.isoformat()
        test_review = Review(id="123", created_at = x, updated_at = x)
        self.assertEqual(test_review.id, "123")
        self.assertEqual(test_review.created_at, test_date)
        self.assertEqual(test_review.updated_at, test_date)

    def test_object_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """
    Unit testing the save method for Review
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
        x = Review()
        sleep(0.05)
        initial_update = x.updated_at
        x.save()
        self.assertLess(initial_update, x.updated_at)

    def test_two_with_save(self):
        x = Review()
        sleep(0.05)
        initial_update = x.updated_at
        x.save()
        subsequent_update = x.updated_at
        self.assertLess(initial_update, subsequent_update)
        sleep(0.05)
        x.save()
        self.assertLess(subsequent_update, x.updated_at)

    def test_for_save_with_arg(self):
        x = Review()
        with self.assertRaises(TypeError):
            x.save(None)

    def test_if_save_updates_file(self):
        x = Review()
        x.save()
        xid = "Review." + x.id
        with open("file.json", "r") as f:
            self.assertIn(xid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """
    Unit testing the to_dict method for Review
    """

    def test_the_type_of_to_dict(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_if_to_dict_has_valid_keys(self):
        x = Review()
        self.assertIn("id", x.to_dict())
        self.assertIn("created_at", x.to_dict())
        self.assertIn("updated_at", x.to_dict())
        self.assertIn("__class__", x.to_dict())

    def test_if_to_dict_has_extra_attr(self):
        x = Review()
        x.middle_name = "kaysee"
        review.test_number = 734
        self.assertEqual("kaysee", x.middle_name)
        self.assertIn("test_number", x.to_dict())

    def test_if_the_to_dict_datetime_attributes_are_strs(self):
        x = Review()
        test_dict = x.to_dict()
        self.assertEqual(str, type(test_dict["id"]))
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test__dict["updated_at"]))

    def test_the_to_dict_output(self):
        x = datetime.today()
        y = Review()
        y.id = "123123"
        y.created_at = y.updated_at = x
        to_dict = {
            'id': '123123',
            '__class__': 'Review',
            'created_at': x.isoformat(),
            'updated_at': x.isoformat(),
        }
        self.assertDictEqual(y.to_dict(), to_dict)

    def test_dunder_dict(self):
        x = Review()
        self.assertNotEqual(x.to_dict(), x.__dict__)

    def test_the_to_dict_with_arg(self):
        x = Review()
        with self.assertRaises(TypeError):
            x.to_dict(None)


if __name__ == "__main__":
    unittest.main()
