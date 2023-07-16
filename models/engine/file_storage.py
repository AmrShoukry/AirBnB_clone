#!/usr/bin/python3
""" File Storage Module """

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        """shows all string representations of a certain class,
         or all if no class is given"""
        result = []
        for key in self.__objects.keys():
            if key.startswith(class_name):
                result.append(self.__objects[key].__str__())
        return result

    def count_class(self, class_name):
        """Count number of classes of a specific type"""
        count = 0
        for key in self.__objects.keys():
            if key.startswith(class_name):
                count += 1
        return count
