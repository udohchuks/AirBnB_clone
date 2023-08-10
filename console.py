#!/usr/bin/python3
"""Console"""
import cmd
import string
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Dictionary(dict):
    """Over riding the dict class"""
    def __missing__(self, key):
        """Output False if key  is not found"""
        return False


my_models = Dictionary()
my_models["BaseModel"] = BaseModel()


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the application."""
        sys.exit(0)

    def help_quit(self):
        """Display help for quit command."""
        print("Quit the application")

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF."""
        print()  # Print a newline before exiting
        return True

    def help_EOF(self):
        """Documentation for EOF"""
        print("EOF- End Of File")

    def do_create(self, arg):
        """Create a new instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show model"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if not my_models[args[0]]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Show model"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if not my_models[args[0]]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Displays all Objects"""
        objects = []
        all_objs = storage.all()
        if not arg:
            for obj in all_objs.values():
                print(obj)
        elif my_models[arg]:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if isinstance(obj, type(my_models[arg])):
                    objects.append(str(obj))
            print(objects)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates Class Instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if not my_models[args[0]]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key in all_objs:
            obj = all_objs[key]
            attr_name = args[2]
            attr_value = args[3]
            attr_value_type = type(getattr(obj, attr_name))
            new_value = attr_value_type(attr_value)
            setattr(obj, attr_name, new_value)
            obj.save()
        else:
            print("** no instance found **")

    def help_create(self):
        """Display help for create"""
        print("Create an Instance of BaseModel")

    def help_create(self):
        """Display help for create command."""
        print("Create a new instance of a specified class.")
        print("Usage: create <class name>")
        print("Example: create BaseModel")

    def help_show(self):
        """Display help for show command."""
        print("Show the string representation of an instance.")
        print("Usage: show <class name> <instance id>")
        print("Example: show BaseModel 1234-1234-1234")

    def help_destroy(self):
        """Display help for destroy command."""
        print("Destroy an instance based on the class name and id.")
        print("Usage: destroy <class name> <instance id>")
        print("Example: destroy BaseModel 1234-1234-1234")

    def help_all(self):
        """Display help for all command."""
        print("Print all instances of a specified class or all classes.")
        print("Usage: all [<class name>]")
        print("Example: all BaseModel")

    def help_update(self):
        """Display help for update command."""
        print("Update an instance's attributes based on class name and id.")
        print("Usage: update <class name> <instance id> <attribute> <value>")
        print("Example: update BaseModel 1234-1234-1234 name 'New Name'")


def run_interactive():
    """Run the interactive command interpreter."""
    cli = HBNBCommand()
    cli.cmdloop()


def run_non_interactive():
    """Run the non-interactive command interpreter."""
    cli = HBNBCommand()
    for line in sys.stdin:
        cli.onecmd(line.strip())


if __name__ == "__main__":
    if sys.stdin.isatty():
        run_interactive()
    else:
        run_non_interactive()
