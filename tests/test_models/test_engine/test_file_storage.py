#!/usr/bin/python3
""" Testing """
import unittest
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """ Test class """

    def setUp(self):
        """ Setting up default initialization """
        self.storage_tester = FileStorage()

    def test_all(self):
        """ Testing __init__(self) """
        self.assertEqual(self.storage_tester.all(), {})


if __name__ == '__main__':
    unittest.main()
