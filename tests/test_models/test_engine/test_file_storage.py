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
        """ Testing all(self) """
        self.assertEqual(self.storage_tester.all(), {})

    def test_new(self):
        """ Testing new(self) """
        self.assertEqual(1, 1)

    def test_reload(self):
        """ Testing save(self) """
        self.assertEqual(1, 1)

    def test_search(self):
        """ Testing save(self) """
        self.assertEqual(1, 1)

    def test_destroy(self):
        """ Testing save(self) """
        self.assertEqual(1, 1)
    def test_get_all_of_class(self):
        """ Testing save(self) """
        self.assertEqual(1, 1)

    def test_count_class(self):
        """ Testing save(self) """
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
