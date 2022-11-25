#!/usr/bin/python3
"""Console Module that controls databases"""

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command processor for this class"""

    prompt = '(hbnb)'
    allowed_classes = ['BaseModel']
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        """
        line = self.parse(arg)[0]
        if line is None:
            print('** class name missing **')
        elif line not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string rep of an instance
        based on the class name
        """
        line = self.parseline(arg)[0]
        args = self.parseline(arg)[1]
        if line is None:
            print('** class name missing **')
        elif line not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args == '':
            print('** instance id missing **')
        else:
            instant_data = models.storage.all().get(line + '.' + args)
            if instant_data is None:
                print('** no instance found **')
            else:
                print(instant_data)
    
    def do_destroy(self, arg):
        """Deletes an instance based on the name and the id
        """

        line = self.parseline(arg)[0]
        args = self.parseline(arg)[1]
        if line is None:
            print('** class name missing **')
        elif line not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args == '':
            print('** instance id missing **')
        else:
            instant_data = models.storage.all().get(line + '.' + args)
            if instant_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

        def do_all(self, arg):
            """Prints all string rep of all instances
            based or not on the class name
            """

            line = self.parseline(arg)[0]
            objec = models.storage.all()
            if line is None:
                for objs in objec:
                    print(str(objec[objs]))
            elif line is self.allowed_classes:
                keys = objec.keys()
                for key in keys:
                    if key.startswith(line):
                        print(str(objec[key]))
            else:
                print("** class doesn't exist **")

        def do_update(self, arg):
            """Updates an instance on the class name
            and id by adding or updating attribute
            """
            

        



if __name__ == '__main__':
    HBNBCommand().cmdloop()


