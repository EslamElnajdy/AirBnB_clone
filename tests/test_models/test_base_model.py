#!/usr/bin/python3
""" Test the base model by using unittest.testcase """
import unittest
from models.base_model import BaseModel


class TestDocumentation(unittest.TestCase):
    """
    test all doc
    """
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

    def test_save(self):
        """
        test doc
        """
        self.assertTrue(len(BaseModel.save.__doc__) > 1)

    def test_to_dict(self):
        """
        test doc
        """
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)


if __name__ == '__main__':
    unittest.main()
