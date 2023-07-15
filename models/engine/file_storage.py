#!/usr/bin/python3
""" File Storage Module """

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ File Storage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        to_be_written = {}
        for key in self.__objects.keys():
            value = self.__objects[key]
            to_be_written[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as file:
            file.write(json.dumps(to_be_written))

    def reload(self):
        """deserializes into __objects from the JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as file:
                file_data = file.read()
                object_list = json.loads(file_data)
                for key in object_list.keys():
                    value = object_list[key]
                    class_type = value["__class__"]
                    self.__objects[key] = eval(class_type)(**value)
