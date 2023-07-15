#!/usr/bin/python3
"""module that houses the user class"""

from models.base_model import BaseModel
from datetime import datetime
from . import storage


class Amenity(BaseModel):
    """this is the class for our amenities"""

    name = ""
