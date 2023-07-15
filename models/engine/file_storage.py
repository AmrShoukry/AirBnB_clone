#!/usr/bin/python3
""" File Storage Module """

import json
import os
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """ File Storage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary """
        return self.__objects

    def update_new(self, obj, search_dict, created_at, updated_at, key, value):
        """creates a new instance of a class as a means of updating it"""
        setattr(obj, key, value)
        obj.created_at = created_at
        obj.updated_at = updated_at
        for dict_key, dict_value in search_dict.items():
            if dict_key == "__class__":
                continue
            setattr(obj, dict_key, dict_value)
        self.new(obj)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    @staticmethod
    def dict_iso_to_datetime(my_dict):
        """takes my_dict and converts the isoformat to datetime format"""
        my_dict["updated_at"] = datetime.fromisoformat(my_dict["updated_at"])
        my_dict["created_at"] = datetime.fromisoformat(my_dict["created_at"])
        return my_dict

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        to_be_written = {}
        for key in self.__objects.keys():
            value = self.__objects[key]
            to_be_written[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(to_be_written))

    def reload(self):
        """deserializes into __objects from the JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                file_data = file.read()
                object_list = json.loads(file_data)
                for key in object_list.keys():
                    value = object_list[key]
                    self.__objects[key] = eval(value["__class__"])(**value)

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

    def count_class(self, class_name):
        """Count number of classes of a specific type"""
        count = 0
        for key in self.__objects.keys():
            if key.startswith(class_name):
                count += 1
        return count
