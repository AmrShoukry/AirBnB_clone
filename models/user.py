#!/usr/bin/python3
"""module that houses the user class"""

from models.base_model import BaseModel
from datetime import datetime
from . import storage


class User(BaseModel):
    """this is the class for our users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """
        this is the string representation of this class
        :return: the string representation of this class
        """
        return f"[User] ({self.id}) {self.__dict__}"

    def save(self):
        """
        TODO
        """
        pass

    def to_dict(self):
        result_dict = super().to_dict()
        result_dict["__class__"] = "User"
        return result_dict
