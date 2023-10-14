#!/usr/bin/python3
""" Test the base model by using unittest.testcase """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestDocumentation(unittest.TestCase):
    """
    test all doc
    """

    def setUp(self):
        self.base_model = BaseModel()

    def test_module(self):
        """
        test doc
        """
        self.assertTrue(len(BaseModel.__module__.__doc__) > 1)

    def test_class(self):
        """
        test doc
        """
        self.assertTrue(len(BaseModel.__doc__) > 1)

    def test_init(self):
        """
        test doc
        """
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)

    def test_str(self):
        """
        test doc
        """
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        b1 = BaseModel()
        # to string format
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)

    def test_save(self):
        """
        test doc
        """
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        # updated_at must be changed
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """
        test doc
        """
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        # check if the dict has all the keys/values
        self.assertTrue("__class__" in obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_two_models_unique_ids(self):
        """
        test doc
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        # Different ids
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """
        test doc
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_timestamps(self):
        """
        test doc
        """
        # right format?
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm._dict_.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

if __name__ == '__main__':
    unittest.main()
