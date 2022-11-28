#!/usr/bin/python3
"""test file storage"""
from models.engine import file_storage
from datetime import datetime
import unittest
import inspect
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
FileStorage = file_storage.FileStorage
classes = {
           "Amenity": Amenity,
           "BaseModel": BaseModel,
           "City": City,
           "Place": Place,
           "Review": Review,
           "State": State,
           "User": User
              }


class TestFileStorageDoc(unittest.TestCase):
    """Tests the documentation and style"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test conformity to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
                                   test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Tests for class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "State class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage"""
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dictio = storage.all()
        self.assertEqual(type(new_dictio), dict)
        self.assertIs(new_dictio, storage._FileStorage__objects)

    def test_new(self):
        """tests if new adds an object"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Test that save properly saves objects"""
        os.remove("file.json")
        storage = FileStorage()
        new_dictio = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dictio[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dictio
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dictio.items():
            new_dictio[key] = value.to_dict()
        string = json.dumps(new_dictio)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
