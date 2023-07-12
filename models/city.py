#!/usr/bin/python3
"""module that houses the user class"""

from models.base_model import BaseModel
from datetime import datetime
from . import storage


class City(BaseModel):
    """this is the class for our cities"""

    state_id = ""
    name = ""

