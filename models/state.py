#!/usr/bin/python3
"""module that houses the user class"""

from models.base_model import BaseModel
from datetime import datetime
from . import storage


class State(BaseModel):
    """this is the class for our states"""

    name = ""
