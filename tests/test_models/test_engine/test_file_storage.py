#!/usr/bin/python3
""" Test filestorage """
import unittest
from models.engine.file_storage import FileStorage


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


if __name__ == '__main__':
    unittest.main()
