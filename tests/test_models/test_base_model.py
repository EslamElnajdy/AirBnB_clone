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
        test doc of the the module
        """
        val = len(BaseModel.__module__.__doc__) > 1
        self.assertTrue(val)

    def test_instance(self):
        """
        test instance
        """
        self.assertIsInstance(BaseModel(), BaseModel)
