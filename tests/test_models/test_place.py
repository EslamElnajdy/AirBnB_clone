#!/usr/bin/python3
""" Test the Place by using unittest.testcase """
import unittest
from models.place import Place
from datetime import datetime


class TestDocumentation(unittest.TestCase):
    """
    test all doc
    """

    def setUp(self):
        self.Place_attr = Place()

    def test_module(self):
        """
        test doc
        """
        self.assertTrue(len(Place.__module__.__doc__) > 1)

    def test_class(self):
        """
        test doc
        """
        self.assertTrue(len(Place.__doc__) > 1)

    def test_init(self):
        """
        test doc
        """
        self.assertTrue(len(Place.__init__.__doc__) > 1)

    def test_name(self):
        self.assertEqual(str, type(self.Place_attr.name))

    def test_user_id(self):
        self.assertEqual(str, type(self.Place_attr.user_id))

    def test_city_id(self):
        self.assertEqual(str, type(self.Place_attr.city_id))

    def test_description(self):
        self.assertEqual(str, type(self.Place_attr.description))

    def test_number_bathrooms(self):
        self.assertEqual(int, type(self.Place_attr.number_bathrooms))

    def test_number_rooms(self):
        self.assertEqual(int, type(self.Place_attr.number_rooms))

    def test_max_guest(self):
        self.assertEqual(int, type(self.Place_attr.max_guest))

    def test_price_by_night(self):
        self.assertEqual(int, type(self.Place_attr.price_by_night))

    def test_latitude(self):
        self.assertEqual(float, type(self.Place_attr.latitude))

    def test_longitude(self):
        self.assertEqual(float, type(self.Place_attr.longitude))

    def test_amenity_ids(self):
        self.assertEqual(list, type(self.Place_attr.amenity_ids))

    def test_str(self):
        """
        test doc
        """
        self.assertTrue(len(Place.__str__.__doc__) > 1)
        b1 = Place()
        # to string format
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)

    def test_save(self):
        """
        test doc
        """
        self.assertTrue(len(Place.save.__doc__) > 1)
        original_updated_at = self.Place_attr.updated_at
        self.Place_attr.save()
        # updated_at must be changed
        self.assertNotEqual(original_updated_at, self.Place_attr.updated_at)

    def test_to_dict(self):
        """
        test doc
        """
        self.assertTrue(len(Place.to_dict.__doc__) > 1)
        obj_dict = self.Place_attr.to_dict()
        self.assertIsInstance(obj_dict, dict)
        # check if the dict has all the keys/values
        self.assertTrue("__class__" in obj_dict)
        self.assertEqual(obj_dict["__class__"], "Place")

    def test_two_models_unique_ids(self):
        """
        test doc
        """
        bm1 = Place()
        bm2 = Place()
        # Different ids
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """
        test doc
        """
        bm1 = Place()
        bm2 = Place()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_timestamps(self):
        """
        test doc
        """
        # right format?
        self.assertIsInstance(self.Place_attr.created_at, datetime)
        self.assertIsInstance(self.Place_attr.updated_at, datetime)

    def test_instantiation_with_kwargs(self):
        """
        test kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

if __name__ == '__main__':
    unittest.main()
