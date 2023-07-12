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
