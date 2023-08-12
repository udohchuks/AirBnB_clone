#!/usr/bin/python3
"""Console"""
import cmd
import string
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
my_models = ["User", "BaseModel"]


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the application."""
        sys.exit(0)

    def help_quit(self):
        """Display help for quit command."""
        print("Quit command to exit the program")

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
        if args[0] not in my_models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        keys_to_iterate = list(objects)
        if key in keys_to_iterate:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Show model"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in my_models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        keys_to_iterate = list(objects)
        if key in keys_to_iterate:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Displays all Objects"""
        objects = []
        all_objs = storage.all()
        keys_to_iterate = list(all_objs.keys())
        if not arg:
            for key in keys_to_iterate:
                obj = all_objs[key]
                objects.append(str(obj))
            print(objects)
        elif arg in my_models:
            for keys in keys_to_iterate:
                obj = all_objs[keys]
                if isinstance(obj, eval(arg)):
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
        if args[0] not in my_models:
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
        keys_to_iterate = list(all_objs)
        if key in keys_to_iterate:
            obj = all_objs[key]
            attr_name = args[2]
            attr_value = args[3]
            attr_value_type = type(getattr(obj, attr_name))
            new_value = attr_value_type(attr_value)
            setattr(obj, attr_name, new_value)
            obj.save()
        else:
            print("** no instance found **")

    def do_count(self, arg):
        """Count object"""
        all_obj = storage.all()
        keys_to_iterate = list(all_obj.keys())
        count = 0
        if not arg:
            print("** class name missing **")
        elif arg in my_models:
            for key in keys_to_iterate:
                obj = all_obj[key]
                if isinstance(obj, eval(arg)):
                    count += 1
            print(count)
        else:
            print("** class doesn't exit**")

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

    def precmd(self, line):
        # if "." in line:
        #     line = line.replace(".", " ").replace("(", "").replace(")", "")\
        #             .replace(",", " ").replace('"', " ")
        #     arg = line.split()
        #     if (len(arg) < 4):
        #         line = "{} {}".format(arg[1], arg[0])
        # return cmd.Cmd.precmd(self, line)
    
    def emptyline(self):
        """Do nothing on an empty line."""
        pass


# def run_interactive():
#     """Run the interactive command interpreter."""
#     cli = HBNBCommand()
#     cli.cmdloop()


# def run_non_interactive():
#     """Run the non-interactive command interpreter."""
#     cli = HBNBCommand()
#     for line in sys.stdin:
#         cli.onecmd(line.strip())


if __name__ == "__main__":
    # if sys.stdin.isatty():
    #     run_interactive()
    # else:
    #     run_non_interactive()
    HBNBCommand().cmdloop()
