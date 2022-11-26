#!/usr/bin/python3
"""unit test for all my files, functions"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import pep8
import os
import uuid
from models import storage
import time
import re
from models.engine.file_storage import FileStorage


class Test_BaseModel(unittest.TestCase):
    """tests All class methods, files,
    functions in BaseModel class
    """
    def setUp(self):
        """ Set up for for object objs of BaseMode"""
        self.BM = BaseModel()

    @classmethod
    def tearDown(cls):
        """
        After all the tests have run the final tearDownClass
        is run
        """

        cls.base.destroy()

    def tearDown(self):
        """Tears down BasModel functions"""
        self.BM.dispose()
        pass

    def test_pep8_base_model_class(self):
        """
        checks BaseModel conform to PEP8
        """

        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "fix pep8")

    def test_pep8_base_model_test(self):
        """test that test/test_models/test_base_model.py conforms to pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "fix pep8")

    def test_save_BaseModel(self):
        """test if save functions"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test__str__BaseModel(self):
        """test the _str method
        that returns (str) a descriptor for BM Class
        """
        String = str(self.BM)
        BMid = '[{}] ({}) {}'.format(self.BM._class_._name_,
                                     self.BM.id, self.BM.__dict__)
        self.assertEqual(True, BMid)
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
        myDict = self.BM.to_dict()
        self.assertEqual(self.base.__class__.__name__, BaseModel)
        self.assertIsInstance(base_dict[created_at], str)
        self.assertIsInstance(base_dict[update-at], str)


if __name__ == '__main__':
    unittest.main()
