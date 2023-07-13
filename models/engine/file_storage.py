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

    def update_new(self, obj, id, created_at, updated_at, key, value):
        """creates a new instance of a class as a means of updating it"""
        setattr(obj, key, value)
        obj.id = id
        obj.created_at = created_at
        obj.updated_at = updated_at
        self.new(obj)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        formatted_dict = self.dict_iso_to_datetime(obj.to_dict())
        text_format = f"[{type(obj).__name__}] ({obj.id}) {formatted_dict}"
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
        """deserializeses into __objects from the JSON file (path: __file_path)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)

    def search(self, key):
        """searches for a class given a key of classname.id"""
        if key in self.__objects:
            return self.__objects[key]
        return False

    def destroy(self, key):
        """destroys an instance of a class given classname and id"""
        if key in self.__objects:
            del self.__objects[key]
            self.save()
            return True
        return False

    def get_all_of_class(self, class_name):
        """shows all of a certain class, or all if no class is given"""
        result = []
        for key in self.__objects.keys():
            if key.startswith(class_name):
                result.append(self.__objects[key])
        return result
