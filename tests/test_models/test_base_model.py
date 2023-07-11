import unittest
import datetime
from models.base_model import BaseModel
""" Testing base model """

class TestBaseModel(unittest.TestCase):
    """ Test class """

    def setUp(self):
        """ Setting up default initialization """
        self.my_model = BaseModel()

    def test_init(self):
        """ Testing __init__(self) """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_str(self):
        """ Testing __str__(self) """
        expected_output = f"[BaseModel] ({self.my_model.id}) ({self.my_model.__dict__})"
        self.assertEqual(str(self.my_model), expected_output)

    def test_to_dict(self):
        """ Testing to_dict(self) """
        expected_dic = self.my_model.to_dict()
        keys = ["id", "created_at", "updated_at", "__class__"]

        for key in keys:
            self.assertIn(key, expected_dic)

    def test_save(self):
        """ Testing save(self) """
        old_update = self.my_model.updated_at
        self.my_model.save(self)
        self.assertNotEqual(old_update, self.my_model.updated_at)
