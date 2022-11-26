#!/usr/bin/python3
"""Console Module that controls databases"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Command processor for this class"""

    prompt = '(hbnb)'
    allowed_classes = {'BaseModel', 'User', 'State', 
            'City', 'Amenity', 'Place', 'Review'}

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
        line = self.parseline(arg)[0]
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
            line = arg.split()
       # line = self.parseline(arg).split
            objs = models.storage.all()
            if line is None:
                print([str(objs[obj]) for obj in objs])
            elif line in self.allowed_classes:
                keys = objs.keys()
                print([str(objs[key]) for key in keys if key.startswith(command)])
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = shlex.split(arg)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()

    def analyze_parameter_value(self, value):
        """Checks a parameter value for an update
        convert to a float number or an integer number.
        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value

if __name__ == '__main__':
    HBNBCommand().cmdloop()
