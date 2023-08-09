#!/usr/bin/python3
"""Console"""
import cmd
import string
import sys


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
