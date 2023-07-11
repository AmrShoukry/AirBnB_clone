#!/usr/bin/python3
"""module that houses the console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """this is the console using the Cmd module"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """quits the program"""
        return True

    def do_EOF(self, line):
        """quits the program"""
        return True

    def emptyline(self):
        """does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
