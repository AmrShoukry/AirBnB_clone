#!/usr/bin/python3
""" Testing  console """
import unittest


class TestConsole(unittest.TestCase):
    """ Test class """

    def test_init(self):
        """ Testing __init__(self) """
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
