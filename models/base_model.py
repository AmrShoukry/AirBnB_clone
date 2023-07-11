#!/usr/bin/python3
"""
this module houses the base_model class
every class inherits from this class
"""

import uuid
import datetime


class BaseModel:
    """
    this is the basemodel class, every class in the airbnb project-
    -is based off of this class
    """

    def __init__(self):
        """
        initializes the BaseModel
        id: random id using uuid4
        created_at, updated_at = datetime.now
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        this is the string representation of this class
        :return: None
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        only modifies the updated_at variable
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        constructs and returns the dict representation of the class
        :return: the dict representation of the class
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = "BaseModel"
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))