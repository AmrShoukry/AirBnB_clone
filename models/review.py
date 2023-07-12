#!/usr/bin/python3
"""module that houses the user class"""

from models.base_model import BaseModel
from datetime import datetime
from . import storage


class Review(BaseModel):
    """this is the class for our reviewes"""

    place_id = ""
    user_id = ""
    text = ""
