#!/usr/bin/python3
"""
this module houses the base_model class
every class inherits from this class
"""

import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """
    this is the basemodel class, every class in the airbnb project-
    -is based off of this class
    """

    def __init__(self, *args, **kwargs):
        """
        initializes the BaseModel
        id: random id using uuid4
        created_at, updated_at = datetime.now
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for arg in kwargs:
                if arg == "__class__":
                    continue
                if arg == "created_at" or arg == "updated_at":
                    vars(self)[arg] = datetime.fromisoformat(kwargs[arg])
                else:
                    vars(self)[arg] = kwargs[arg]

    def __str__(self):
        """
        this is the string representation of this class
        :return: the string representation of this class
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        only modifies the updated_at variable
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        constructs and returns the dict representation of the class
        :return: the dict representation of the class
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = f"{type(self).__name__}"
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict
