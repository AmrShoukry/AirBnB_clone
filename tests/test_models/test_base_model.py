import unittest
from datetime import datetime
from models.base_model import BaseModel
""" Testing base model """


class TestBaseModel(unittest.TestCase):
    """ Test class """

    def setUp(self):
        """ Setting up default initialization """
        self.my_model1 = BaseModel()
        self.my_model2 = BaseModel(
            id="1",
            __class__="Amr",
            created_at="2003-08-03T00:00:00",
            updated_at="2023-07-11T00:00:00",
            Age=20
        )

    def test_init(self):
        """ Testing __init__(self) """
        self.assertIsInstance(self.my_model1.id, str)
        self.assertIsInstance(self.my_model1.created_at, datetime)
        self.assertIsInstance(self.my_model1.updated_at, datetime)

        self.assertIsInstance(self.my_model2.id, str)
        self.assertIsInstance(self.my_model2.created_at, datetime)
        self.assertIsInstance(self.my_model2.updated_at, datetime)
        self.assertIsInstance(self.my_model2.Age, int)

        # with self.assertRaises(ValueError):
        #     BaseModel(
        #         id = "1",
        #         __class__ = "Amr",
        #         created_at = "2003-08-03",
        #         updated_at = "2023-07-11",
        #         Age = 20
        #     )

    def test_str(self):
        """ Testing __str__(self) """
        id1 = self.my_model1.id
        expected_output1 = f"[BaseModel] ({id1}) {self.my_model1.__dict__}"
        self.assertEqual(str(self.my_model1), expected_output1)

        id2 = self.my_model2.id
        expected_output2 = f"[BaseModel] ({id2}) {self.my_model2.__dict__}"
        self.assertEqual(str(self.my_model2), expected_output2)

    def test_to_dict(self):
        """ Testing to_dict(self) """
        expected_dic1 = self.my_model1.to_dict()
        keys = ["id", "created_at", "updated_at", "__class__"]
        for key in keys:
            self.assertIn(key, expected_dic1)

        # expected_dict2 = self.my_model2.to_dict()
        # class_dict2 = {"__class__": "BaseModel"}
        # keys2 = list(self.__dict__.keys().update({class_dict2}))
        # for key in keys2:
        #     self.assertIn(key, expected_dict2)

    def test_save(self):
        """ Testing save(self) """
        old_update1 = self.my_model1.updated_at
        self.my_model1.save()
        self.assertNotEqual(old_update1, self.my_model1.updated_at)

        old_update2 = self.my_model2.updated_at
        self.my_model2.save()
        self.assertNotEqual(old_update2, self.my_model2.updated_at)
