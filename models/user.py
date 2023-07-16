#!/usr/bin/python3
"""module that houses the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """this is the class for our users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
