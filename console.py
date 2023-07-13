#!/usr/bin/python3
"""module that houses the console"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
from datetime import datetime
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """this is the console using the Cmd module"""
    prompt = "(hbnb) "
    my_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def check_arg_validity_classes(self, args):
        if len(args) < 1 or args[0] == '':
            print("** class name missing **")
            return True
        elif args[0] not in self.my_classes:
            print("** class doesn't exist **")
            return True
        return False

    def check_arg_validity_classes_ids(self, args):
        if self.check_arg_validity_classes(args):
            return True
        elif len(args) < 2:
            print("** instance id missing **")
            return True
        else:
            search_key = '.'.join(args[:2])
            search_result = storage.search(search_key)
            if search_result is False:
                print("** no instance found **")
                return True
        return search_key

    def check_arg_validity_classes_attributes(self, args):
        search_key = self.check_arg_validity_classes_ids(args)
        if search_key is True:
            return True
        elif len(args) < 3:
            print("** attribute name missing **")
            return True
        elif len(args) < 4:
            print("** value missing **")
            return True
        elif args[2] == "id" or args[2] == "created_at" or args[2] == "updated_at":
            return True
        return search_key

    def do_quit(self, line):
        """quits the program"""
        return True

    def do_create(self, line):
        args = line.split(" ")
        if self.check_arg_validity_classes(args):
            pass
        else:
            created_class = self.my_classes[line]()
            print(created_class.id)
            storage.new(created_class)
            storage.save()

    def do_show(self, line):
        args = line.split(" ")
        search_key = self.check_arg_validity_classes_ids(args)
        if search_key is not True:
            search_result = storage.search(search_key)
            print(search_result)

    def do_destroy(self, line):
        args = line.split(" ")
        search_key = self.check_arg_validity_classes_ids(args)
        if search_key is not True:
            storage.destroy(search_key)

    def do_all(self, line):
        args = line.split(" ")
        if args[0] == "" or self.check_arg_validity_classes(args) is False:
            result = storage.get_all_of_class(args[0])
            for class_instance in result:
                print(class_instance)

    def do_update(self, line):
        args = line.split(" ")
        search_key = self.check_arg_validity_classes_attributes(args)
        if search_key is not True:
            search_instance = storage.search(search_key)
            search_dict_text = search_instance.split(")", 1)[1]

            date_string = re.search(r"'created_at': datetime\.datetime\((.*?)\)", search_dict_text)
            datetime_str = date_string.group(1)
            created_at = datetime.strptime(datetime_str, "%Y, %m, %d, %H, %M, %S, %f")

            date_string = re.search(r"'updated_at': datetime\.datetime\((.*?)\)", search_dict_text)
            datetime_str = date_string.group(1)
            updated_at = datetime.strptime(datetime_str, "%Y, %m, %d, %H, %M, %S, %f")

            search_dict_text = re.sub(r"(, )?'created_at': datetime\.datetime\(.*?\)", "", search_dict_text)
            search_dict_text = re.sub(r"(, )?'updated_at': datetime\.datetime\(.*?\)", "", search_dict_text)
            search_dict_text = search_dict_text.replace("'", "\"")

            search_dict = json.loads(search_dict_text)

            id = search_dict["id"]

            storage.destroy(search_key)

            created_class = self.my_classes[args[0]]()
            
            storage.update_new(created_class, id, created_at, updated_at, args[2], args[3])                
            storage.save()



    def do_EOF(self, line):
        """quits the program"""
        return True

    def emptyline(self):
        """does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
