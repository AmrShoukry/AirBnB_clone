#!/usr/bin/python3
"""module that houses the user class"""

from models.base_model import BaseModel


class City(BaseModel):
    """this is the class for our cities"""

    state_id = ""
    name = ""
