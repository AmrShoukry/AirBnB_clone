#!/usr/bin/python3
""" File Storage Module """

import json
import os


class FileStorage:
    """ File Storage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        text_format = f"[BaseModel] ({obj.id}) {obj.to_dict()}"
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = text_format

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """ deserialize """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
