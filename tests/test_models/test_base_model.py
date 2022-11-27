#!/usr/bin/python3
"""unitTest for behaviour and doc type"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import pep8
import os
import uuid
from models import storage
import time
import models
from unittest import mock
import inspect
module_doc = models.base_model.__doc__
BaseModel = models.base_model.BaseModel


class TestBaseModel_docs(unittest.TestCase):
    """tests All class methods, files,
    functions and docStyle in BaseModel class
    """

    @classmethod
    def setUpClass(self):
        """ Set up for for object objs of BaseMode"""
        self.BM = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_base_model_conformity(self):
        """
        checks BaseModel conform to PEP8
        """

        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "fix pep8")

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_funct_docstrings(self):
        """Test for docstrings in BaseModel"""
        for funct in self.BM:
            with self.subTest(function=funct):
                self.assertIsNot(
                    funct[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(funct[0])
                )
                self.assertTrue(
                    len(funct[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(funct[0])
                )


class TestBaseModel(unittest.TestCase):
    """tests the class BaseModel"""

    @mock.patch('models.storage')
    def test_intantiationBaseModel(self, mock_storage):
        """test odject creation status"""
        insta = BaseModel()
        self.assertIs(type(inst), BaseModel)
        insta.name = "School"
        insta.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, insta.__dict__)
                self.assertIs(type(insta.__dict__[attr]), typ)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(insta.name, "School")
        self.assertEqual(insta.number, 89)

    def test_save_BaseModel(self):
        """test if save functions"""
        BM = BaseModel()
        self.BM.save()
        self.assertNotEqual(self.BM.created_at, self.BM.updated_at)

    def test__str__BaseModel(self):
        """test the _str method
        that returns (str) a descriptor for BM Class
        """
        String = str(self.BM)
        BM.id = '[{}] ({}) {}'.format(self.BM._class_._name_,
                                     self.BM.id, self.BM.__dict__)
        self.assertEqual(True, BM.id)
        self.assertEqual(True, 'creaed_at')
        self.assertEqual(True, 'updated_at')
        self.assertEqual(True, 'datetime')

    def test_uu_id_BaseModel(self):
        """
        Test for unique ids of user
        Test that first and second are not equal
        """
        BM1 = BaseModel()
        BM2 = BaseModel()
        self.assertNotEqual(BM1.id, BM2.id)

    def test_id__type__str(self):
        """Checks if id is a string"""
        self.assertEqual(type(self.BM.id), str)

    def test_created_time(self):
        """
        Checks timedate format is the correct DateTime
        added datetime."now"

        """
        BM = BaseModel()
        self.assertIsInstance(BM.created_at, datetime)

    def test_updated_time(self):
        """Checks updated dateTime format is the correct DateTime"""
        BM = BaseModel()
        self.assertIsInstance(BM.updated_at, datetime)

    def test_to_dict_BaseModel(self):
        """Checks for working dictionary methods"""
        BM = BaseModel()
        myDict = self.BM.to_dict()
        self.assertEqual(self.BM.__class__.__name__, BaseModel)
        self.assertIsInstance(BM_dict[created_at], str)
        self.assertIsInstance(BM_dict[update-at], str)
