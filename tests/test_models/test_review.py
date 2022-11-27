#!/usr/bin/python3
"""
Created on Sunday Dec  5 15:43:09 2020
@author: Geoffy1
"""

import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.review import Review


class TestReview(unittest.TestCase):
    """
    class for testing Review class methd
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_Review(self):
        """
        Test conformity to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Review(self):
        """
        Test conformity to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring doc exist
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring doc exist
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methds docstring doc exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        self.UR = Review()

    def tearDown(self):
        self.UR = None

    def test_type(self):
        """test methd for type testing of review
        """
        self.assertIsInstance(self.UR, Review)
        self.assertEqual(type(self.UR), Review)
        self.assertEqual(issubclass(self.UR.__class__, Review), True)
        self.assertEqual(isinstance(self.UR, Review), True)

    def test_place_id_type(self):
        """tests the pl_id class attr type of Review
        """
        self.assertEqual(type(Review.place_id), str)

    def test_user_id_type(self):
        """tests the u_id class attr type of Review
        """
        self.assertEqual(type(Review.user_id), str)

    def test_text_type(self):
        """tests the text class attr type of Review
        """
        self.assertEqual(type(Review.text), str)

    def test_string_return(self):
        """tests the str methd
        """
        string = str(self.UR)
        Rid = "[{}] ({})".format(self.UR.__class__.__name__,
                                 self.UR.id)
        test = URid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime.datetime" in string
        self.assertEqual(True, test)

    def test_to_dict(self):
        """tests to_dict methd
        """
        my_dict = self.UR.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.UR.created_at.isoformat())
        self.assertEqual(datetime, type(self.UR.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.UR.__class__.__name__)
        self.assertEqual(my_dict['id'], self.UR.id)

    def test_to_dict_more(self):
        """tests to_dict methd
        """
        my_dict = self.UR.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.UR.created_at, time)

    def test_from_dict_basic(self):
        """tests the from_dict methd
        """
        my_dict = self.UR.to_dict()
        UR1 = self.UR.__class__(**my_dict)
        self.assertEqual(UR1.id, self.UR.id)
        self.assertEqual(UR1.updated_at, self.UR.updated_at)
        self.assertEqual(UR1.created_at, self.UR.created_at)
        self.assertEqual(UR1.__class__.__name__,
                         self.UR.__class__.__name__)

    def test_from_dict_hard(self):
        """test from_dict method
        """
        self.UR.name = 'Meco'
        my_dict = self.UR.to_dict()
        self.assertEqual(my_dict['name'], 'Meco')
        UR1 = self.UR.__class__(**my_dict)
        self.assertEqual(UR1.created_at, self.UR.created_at)

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        UR1 = self.UR.__class__()
        UR2 = self.UR.__class__()
        self.assertNotEqual(self.UR.id, UR1.id)
        self.assertNotEqual(self.UR.id, UR2.id)

    def test_id_type_string(self):
        """test id of the class is a str
        """
        self.assertEqual(type(self.UR.id), str)

    def test_updated_time(self):
        """test time is updated
        """
        time1 = self.UR.updated_at
        self.UR.save()
        time2 = self.UR.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
