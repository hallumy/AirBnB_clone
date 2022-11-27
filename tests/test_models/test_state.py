#!/usr/bin/python3
"""
Created on Sunday Nov  27 17:15:09 2022
@authors: Geoffy1 , hallumy
"""
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from models.state import State
from contextlib import redirect_stdout
St = State()


class TestState(unittest.TestCase):
    """
    class for testing State class' methods
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.state_fn = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_State(self):
        """
        Test to conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """
        Test to conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for module docstring
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests for docstring documentation
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for docstring doc
        """
        for func in self.state_fn:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """set up methd for State class
        """
        self.St = State()

    def tearDown(self):
        """initialized methd for State class
        """
        self.St = None

    def test_type(self):
        """test method for type testing
        """
        self.assertIsInstance(self.St, State)
        self.assertEqual(type(self.St), State)
        self.assertEqual(issubclass(self.St.__class__, State), True)
        self.assertEqual(isinstance(self.St, State), True)

    def test_name_type(self):
        """tests the type of state attr
        """
        self.assertEqual(type(State.name), str)

    def test_string_return(self):
        """tests the string methd
        """
        string = str(self.St)
        St.id = "[{}] ({})".format(self.St.__class__.__name__,
                                   self.St.id)
        test = St.id in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime.datetime" in string
        self.assertEqual(True, test)

    def test_to_dict(self):
        """tests to_dict method
        """
        my_dict = self.St.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.St.created_at.isoformat())
        self.assertEqual(datetime, type(self.St.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.St.__class__.__name__)
        self.assertEqual(my_dict['id'], self.St.id)

    def test_to_dict_more(self):
        """tests to_dict method
        """
        St = State()
        my_dict = self.St.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.St.created_at, time)

    def test_from_dict_basic(self):
        """tests from_dict method
        """
        my_dict = self.St.to_dict()
        St1 = self.St.__class__(**my_dict)
        self.assertEqual(St1.id, self.St.id)
        self.assertEqual(St1.updated_at, self.St.updated_at)
        self.assertEqual(St1.created_at, self.St.created_at)
        self.assertEqual(St1.__class__.__name__,
                         self.St.__class__.__name__)

    def test_from_dict_hard(self):
        """test from_dict method for class objects
        """
        self.St.name = 'Hallumy'
        my_dict = self.St.to_dict()
        self.assertEqual(my_dict['name'], 'Hallumy')
        St1 = self.St.__class__(**my_dict)
        self.assertEqual(St1.created_at, self.St.created_at)
