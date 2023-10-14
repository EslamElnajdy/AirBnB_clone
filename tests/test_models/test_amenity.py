#!/usr/bin/python3
""" Test the Amenity by using unittest.testcase """
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestDocumentation(unittest.TestCase):
    """
    test all doc
    """

    def setUp(self):
        self.Amenity_attr = Amenity()

    def test_module(self):
        """
        test doc
        """
        self.assertTrue(len(Amenity.__module__.__doc__) > 1)

    def test_class(self):
        """
        test doc
        """
        self.assertTrue(len(Amenity.__doc__) > 1)

    def test_init(self):
        """
        test doc
        """
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)

    def test_name(self):
        self.assertEqual(str, type(self.Amenity_attr.name))

    def test_str(self):
        """
        test doc
        """
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        b1 = Amenity()
        # to string format
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)

    def test_save(self):
        """
        test doc
        """
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        original_updated_at = self.Amenity_attr.updated_at
        self.Amenity_attr.save()
        # updated_at must be changed
        self.assertNotEqual(original_updated_at, self.Amenity_attr.updated_at)

    def test_to_dict(self):
        """
        test doc
        """
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)
        obj_dict = self.Amenity_attr.to_dict()
        self.assertIsInstance(obj_dict, dict)
        # check if the dict has all the keys/values
        self.assertTrue("__class__" in obj_dict)
        self.assertEqual(obj_dict["__class__"], "Amenity")

    def test_two_models_unique_ids(self):
        """
        test doc
        """
        bm1 = Amenity()
        bm2 = Amenity()
        # Different ids
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """
        test doc
        """
        bm1 = Amenity()
        bm2 = Amenity()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_timestamps(self):
        """
        test doc
        """
        # right format?
        self.assertIsInstance(self.Amenity_attr.created_at, datetime)
        self.assertIsInstance(self.Amenity_attr.updated_at, datetime)

    def test_instantiation_with_kwargs(self):
        """
        test kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

if __name__ == '__main__':
    unittest.main()
