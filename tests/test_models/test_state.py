#!/usr/bin/python3
""" Test the State by using unittest.testcase """
import unittest
from models.state import State
from datetime import datetime


class TestDocumentation(unittest.TestCase):
    """
    test all doc
    """

    def setUp(self):
        self.state_attr = State()

    def test_module(self):
        """
        test doc
        """
        self.assertTrue(len(State.__module__.__doc__) > 1)

    def test_class(self):
        """
        test doc
        """
        self.assertTrue(len(State.__doc__) > 1)

    def test_init(self):
        """
        test doc
        """
        self.assertTrue(len(State.__init__.__doc__) > 1)

    def test_name(self):
        self.assertEqual(str, type(self.state_attr.name))

    def test_str(self):
        """
        test doc
        """
        self.assertTrue(len(State.__str__.__doc__) > 1)
        b1 = State()
        # to string format
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)

    def test_save(self):
        """
        test doc
        """
        self.assertTrue(len(State.save.__doc__) > 1)
        original_updated_at = self.state_attr.updated_at
        self.state_attr.save()
        # updated_at must be changed
        self.assertNotEqual(original_updated_at, self.state_attr.updated_at)

    def test_to_dict(self):
        """
        test doc
        """
        self.assertTrue(len(State.to_dict.__doc__) > 1)
        obj_dict = self.state_attr.to_dict()
        self.assertIsInstance(obj_dict, dict)
        # check if the dict has all the keys/values
        self.assertTrue("__class__" in obj_dict)
        self.assertEqual(obj_dict["__class__"], "State")

    def test_two_models_unique_ids(self):
        """
        test doc
        """
        bm1 = State()
        bm2 = State()
        # Different ids
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """
        test doc
        """
        bm1 = State()
        bm2 = State()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_timestamps(self):
        """
        test doc
        """
        # right format?
        self.assertIsInstance(self.state_attr.created_at, datetime)
        self.assertIsInstance(self.state_attr.updated_at, datetime)

    def test_instantiation_with_kwargs(self):
        """
        test kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

if __name__ == '__main__':
    unittest.main()
