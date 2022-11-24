#!/usr/bin/python3
"""Console Module that controls databases"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command processor for this class"""

    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        
        return True

    def emptyline(self):
        """When an empty line is entered nothing
        will be executed
        """

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()


