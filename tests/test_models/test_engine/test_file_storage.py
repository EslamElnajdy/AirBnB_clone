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
