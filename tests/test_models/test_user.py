#!/usr/bin/python3
""" Test the User by using unittest.testcase """
import unittest
from models.user import User
from datetime import datetime


class TestDocumentation(unittest.TestCase):
    """
    test all doc
    """

    def setUp(self):
        self.User_attr = User()

    def test_module(self):
        """
        test doc
        """
        self.assertTrue(len(User.__module__.__doc__) > 1)

    def test_class(self):
        """
        test doc
        """
        self.assertTrue(len(User.__doc__) > 1)

    def test_init(self):
        """
        test doc
        """
        self.assertTrue(len(User.__init__.__doc__) > 1)

    def test_email(self):
        self.assertEqual(str, type(self.User_attr.email))

    def test_password(self):
        self.assertEqual(str, type(self.User_attr.password))

    def test_first_name(self):
        self.assertEqual(str, type(self.User_attr.first_name))

    def test_last_name(self):
        self.assertEqual(str, type(self.User_attr.last_name))

    def test_str(self):
        """
        test doc
        """
        self.assertTrue(len(User.__str__.__doc__) > 1)
        b1 = User()
        # to string format
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)

    def test_save(self):
        """
        test doc
        """
        self.assertTrue(len(User.save.__doc__) > 1)
        original_updated_at = self.User_attr.updated_at
        self.User_attr.save()
        # updated_at must be changed
        self.assertNotEqual(original_updated_at, self.User_attr.updated_at)

    def test_to_dict(self):
        """
        test doc
        """
        self.assertTrue(len(User.to_dict.__doc__) > 1)
        obj_dict = self.User_attr.to_dict()
        self.assertIsInstance(obj_dict, dict)
        # check if the dict has all the keys/values
        self.assertTrue("__class__" in obj_dict)
        self.assertEqual(obj_dict["__class__"], "User")

    def test_two_models_unique_ids(self):
        """
        test doc
        """
        bm1 = User()
        bm2 = User()
        # Different ids
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """
        test doc
        """
        bm1 = User()
        bm2 = User()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_timestamps(self):
        """
        test doc
        """
        # right format?
        self.assertIsInstance(self.User_attr.created_at, datetime)
        self.assertIsInstance(self.User_attr.updated_at, datetime)

    def test_instantiation_with_kwargs(self):
        """
        test kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

if __name__ == '__main__':
    unittest.main()
