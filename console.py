#!/usr/bin/python3
"""
A program called console.py that contains
the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """initializing HBNBCommand"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
