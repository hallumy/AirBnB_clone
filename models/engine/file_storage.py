#!/usr/bin/python3
"""class FileStorage"""

import json
from os import path
from models.base_model import BaseModel

class FileStorage:
    """File storage class
    Contains __file_path which is the path of json file
    that the contents of the __object variable will be
    stored
    __objects dictionary stores all instance data
    """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """Gets the object information
        and returns the content of the object class attribute
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in the __objects class attribute the
        instance data with a key as <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the content of __objects class
        attributes to the path of __file_path class
        attribute in json format with the created_at
        and updated_at format
        """
        json_to_dic = {}
        for key, value in FileStorage.__objects.items():
            json_to_dic[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding= 'utf-8') as f:
           json.dump(json_to_dic, f)

    def reload(self):
        """If the __file_path exists deserialization of
        json file to __objects, else does nothing
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding= 'utf-8') as f:
                json_to_dic = json.load(f)
                for key, value in json_to_dic.items():
                    self.__objects[key] = eval(value["__class__"])(**value)

