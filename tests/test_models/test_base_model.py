
""" Test the base model by using unittest.testcase """
import unittest

from models.base_model import BaseModel


class TestDocumentation(unittest.TestCase):
    """
    test all doc
    """
    def test_modele(self):
        """
        test doc of the the module
        """
        self.assertTrue(len(BaseModel.__module__.__doc__) > 1)
