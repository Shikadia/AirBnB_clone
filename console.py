#!/usr/bin/python3
"""HBNB console class."""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    command line interpreter
    Attributes:
        prompt (str): command prompt for AirBnB
    """
    prompt = "(hbnb): "
    def do_quit(self, arg):
        """Exits the program when called."""
        return True

    def do_EOF(self, arg):
        """Exits the program when reached."""
        print("")
        return True

    def emptyline(self):
        """Execute nothing when an empty line is passed."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
