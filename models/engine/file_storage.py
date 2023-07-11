#!/usr/bin/python3
""" File Storage Module """

import json
import os
from datetime import datetime


class FileStorage:
    """ File Storage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        formatted_dict = self.dict_iso_to_datetime(obj.to_dict())
        text_format = f"[BaseModel] ({obj.id}) {formatted_dict}"
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = text_format

    @staticmethod
    def dict_iso_to_datetime(my_dict):
        """takes my_dict and converts the isoformat to datetime format"""
        my_dict["updated_at"] = datetime.fromisoformat(my_dict["updated_at"])
        my_dict["created_at"] = datetime.fromisoformat(my_dict["created_at"])
        return my_dict

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """ deserialize """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)

    def search(self, key):
        if key in self.__objects:
            return self.__objects[key]
        return False
