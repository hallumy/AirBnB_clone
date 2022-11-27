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
import re

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
            argl = parse(arg)
            if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                objl = []
                for obj in storage.all().values():
                    if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                        objl.append(obj.__str__())
                    elif len(argl) == 0:
                        objl.append(obj.__str__())
                print(objl)

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

    def get_objects(self, instance=''):
        """Gets the elements created by the console
        This method takes care of obtaining the information
        of all the instances created in the file `objects.json`
        that is used as the storage engine.
        """
        objects = models.storage.all()

        if instance:
            keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]

        return [str(val) for key, val in objects.items()]

    def default(self, line):
        """When the command prefix is not recognized, this method
        looks for whether the command entered has the syntax:
        """
        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]

            if class_name in self.allowed_classes:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
