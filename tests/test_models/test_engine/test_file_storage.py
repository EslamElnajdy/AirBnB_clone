#!/usr/bin/python3
""" Test filestorage """
import unittest
import os

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.user import User
from models.city import City


class TestDocuementation(unittest.TestCase):
    """
    test all doc
    """
    def test_module(self):
        """
        test doc
        """
        self.assertTrue(len(FileStorage.__module__.__doc__) > 1)

    def test_class(self):
        """
        test doc
        """
        self.assertTrue(len(FileStorage.__doc__) > 1)

    def test_all(self):
        """
        test doc
        """
        self.assertTrue(len(FileStorage.all.__doc__) > 1)

    def test_new(self):
        """
        test doc
        """
        self.assertTrue(len(FileStorage.new.__doc__) > 1)

    def test_save(self):
        """
        test doc
        """
        self.assertTrue(len(FileStorage.save.__doc__) > 1)

    def test_reload(self):
        """
        test doc
        """
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)


class TestAttributes(unittest.TestCase):
    """
    test attr
    """
    def test_instance(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_filepath(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestMethod(unittest.TestCase):
    """
    test method
    """

    def setUp(self):
        """
        setup method
        """
        self.storage = FileStorage()
        self.b = BaseModel()
        self.a = Amenity()
        self.r = Review()
        self.p = Place()
        self.s = State()
        self.u = User()
        self.c = City()
        self.storage.save()

    def tearDown(self):
        """
        teardown method
        """
        del self.storage
        del self.b
        del self.a
        del self.r
        del self.p
        del self.s
        del self.u
        del self.c
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_all(self):
        """
        teat on all()
        """
        obj = self.storage.all()
        self.assertEqual(dict, type(obj))
        self.assertIsNotNone(obj)

    def test_new(self):
        """
        test on new()
        """
        self.storage.new(self.b)
        self.storage.new(self.a)
        self.storage.new(self.r)
        self.storage.new(self.p)
        self.storage.new(self.s)
        self.storage.new(self.u)
        self.storage.new(self.c)
        self.storage.save()
        self.assertIn("BaseModel." + self.b.id, self.storage.all().keys())
        self.assertIn(self.b, self.storage.all().values())
        self.assertIn("Amenity." + self.a.id, self.storage.all().keys())
        self.assertIn(self.a, self.storage.all().values())
        self.assertIn("Review." + self.r.id, self.storage.all().keys())
        self.assertIn(self.r, self.storage.all().values())
        self.assertIn("Place." + self.p.id, self.storage.all().keys())
        self.assertIn(self.p, self.storage.all().values())
        self.assertIn("State." + self.s.id, self.storage.all().keys())
        self.assertIn(self.s, self.storage.all().values())
        self.assertIn("User." + self.u.id, self.storage.all().keys())
        self.assertIn(self.u, self.storage.all().values())
        self.assertIn("City." + self.c.id, self.storage.all().keys())
        self.assertIn(self.c, self.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            self.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            self.storage.new(None)

    def test_save(self):
        """
        test on save()
        """
        self.storage.new(self.b)
        self.storage.new(self.a)
        self.storage.new(self.r)
        self.storage.new(self.p)
        self.storage.new(self.s)
        self.storage.new(self.u)
        self.storage.new(self.c)
        self.storage.save()

        with open('file.json', 'r') as f:
            text = f.read()

        self.assertIn("BaseModel." + self.b.id, text)
        self.assertIn("Amenity." + self.a.id, text)
        self.assertIn("Review." + self.r.id, text)
        self.assertIn("Place." + self.p.id, text)
        self.assertIn("State." + self.s.id, text)
        self.assertIn("User." + self.u.id, text)
        self.assertIn("City." + self.c.id, text)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload(self):
        """
        test on reload()
        """
        self.storage.new(self.b)
        self.storage.new(self.a)
        self.storage.new(self.r)
        self.storage.new(self.p)
        self.storage.new(self.s)
        self.storage.new(self.u)
        self.storage.new(self.c)
        self.storage.save()
        self.storage.reload()

        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + self.b.id, objs)
        self.assertIn("Amenity." + self.a.id, objs)
        self.assertIn("Review." + self.r.id, objs)
        self.assertIn("Place." + self.p.id, objs)
        self.assertIn("State." + self.s.id, objs)
        self.assertIn("User." + self.u.id, objs)
        self.assertIn("City." + self.c.id, objs)

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            self.storage.reload(None)


if __name__ == '__main__':
    unittest.main()
