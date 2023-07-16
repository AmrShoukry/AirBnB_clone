#!/usr/bin/python3
""" Testing """
import unittest
from datetime import datetime
from models.user import User

class TestConsole(unittest.TestCase):
    """ Test class """

    def setUp(self):
        """ Setting up default initialization """
        self.my_model1 = User()
        self.my_model1.email = "one"
        self.my_model1.first_name = "two"
        self.my_model1.last_name = "three"
        self.my_model1.password = "four"
        self.my_model2 = User(
            id="1",
            __class__="Amr",
            created_at="2003-08-03T00:00:00",
            updated_at="2023-07-11T00:00:00",
            Age=20
        )

    def test_init(self):
        """ Testing __init__(self) """
        self.assertIsInstance(self.my_model1, User)
        self.assertIsInstance(self.my_model1.id, str)
        self.assertIsInstance(self.my_model1.created_at, datetime)
        self.assertIsInstance(self.my_model1.updated_at, datetime)

        self.assertIsInstance(self.my_model2, User)
        self.assertIsInstance(self.my_model2.id, str)
        self.assertIsInstance(self.my_model2.created_at, datetime)
        self.assertIsInstance(self.my_model2.updated_at, datetime)
        self.assertIsInstance(self.my_model2.Age, int)



if __name__ == '__main__':
    unittest.main()
