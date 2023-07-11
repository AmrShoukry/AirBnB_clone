#!/usr/bin/python3
"""module that houses the console"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """this is the console using the Cmd module"""
    prompt = "(hbnb)"
    my_classes = {
        "BaseModel": BaseModel
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
        return False

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
        if self.check_arg_validity_classes_ids(args):
            pass
        else:
            search_key = '.'.join(args[:2])
            search_result = storage.search(search_key)
            if search_result is False:
                print("** no instance found **")
            else:
                print(search_result)

    def do_destroy(self, line):
        args = line.split(" ")
        if self.check_arg_validity_classes_ids(args):
            pass
        else:
            search_key = '.'.join(args[:2])
            if storage.destroy(search_key) is False:
                print("** no instance found **")

    def do_all(self, line):
        args = line.split(" ")
        if self.check_arg_validity_classes(args):
            result = storage.get_all_of_class(args[0])
            for class_instance in result:
                print(class_instance)

    def do_EOF(self, line):
        """quits the program"""
        return True

    def emptyline(self):
        """does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
