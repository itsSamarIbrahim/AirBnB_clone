#!/usr/bin/python3
"""
A program called console.py that contains
the entry point of the command interpreter
"""
import cmd
import json
from models.base_model import BaseModel


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        try:
            with open("file.json", "r") as file:
                all_objs = json.load(file)
                key = args[0] + "." + args[1]
                if key in all_objs:
                    print(all_objs[key])
                else:
                    print("** no instance found **")
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        try:
            with open("file.json", "r") as file:
                all_objs = json.load(file)
            key = args[0] + "." + args[1]
            if key in all_objs:
                del all_objs[key]
                with open("file.json", "w") as file:
                    json.dump(all_objs, file)
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        try:
            with open("file.json", "r") as file:
                all_objs = json.load(file)
                if arg and arg not in ["BaseModel"]:
                    print("** class doesn't exist **")
                    return
                else:
                    obj_list = [str(v) for k, v in all_objs.items()]
                    print(obj_list)
        except Exception as e:
            print(e)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            with open("file.json", "r") as file:
                all_objs = json.load(file)
            key = args[0] + "." + args[1]
            if key in all_objs:
                obj = all_objs[key]
                setattr(obj, args[2], args[3])
                all_objs[key] = obj
                with open("file.json", "w") as file:
                    json.dump(all_objs, file)
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
