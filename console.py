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

    def do_quit(self, line):
        """quits the program"""
        return True

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line not in self.my_classes:
            print("** class doesn't exist **")
        else:
            created_class = self.my_classes[line]()
            storage.save()

    def do_EOF(self, line):
        """quits the program"""
        return True

    def emptyline(self):
        """does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
