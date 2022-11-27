#!/usr/bin/python3
"""
the TestUser class methods
"""
import time
from datetime import datetime
import inspect
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City’s docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class testUser(unittest.TestCase):
    """Test the User"""
    def test_is_subclass(self):
        """Test User a subclass"""
        us = User()
        self.assertIsInstance(us, BaseModel)
        self.assertTrue(hasattr(us, "id"))
        self.assertTrue(hasattr(us, "created_at"))
        self.assertTrue(hasattr(us, "updated_at"))

    def test_email_attr(self):
        """Test that User has email, and an empty string"""
        us = User()
        self.assertTrue(hasattr(us, "email"))
        self.assertEqual(us.email, "")

    def test_password_attr(self):
        """Test that User has pswd, and an empty string"""
        us = User()
        self.assertTrue(hasattr(us, "password"))
        self.assertEqual(us.password, "")

    def test_first_name_attr(self):
        """Test that User has first_name, and an empty string"""
        us = User()
        self.assertTrue(hasattr(us, "first_name"))
        self.assertEqual(us.first_name, "")

    def test_last_name_attr(self):
        """Test for User last_name and is an empty string"""
        us = User()
        self.assertTrue(hasattr(us, "last_name"))
        self.assertEqual(us.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary"""
        us = User()
        new_dic = us.to_dict()
        self.assertEqual(type(new_dic), dict)
        for attr in us.__dict__:
            self.assertTrue(attr in new_dic)
            self.assertTrue("__class__" in new_dic)

    def test_to_dict_values(self):
        """test values in dict returned from to_dict"""
        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        us = User()
        new_dic = us.to_dict()
        self.assertEqual(new_dic["__class__"], "User")
        self.assertEqual(type(new_dic["created_at"]), str)
        self.assertEqual(type(new_dic["updated_at"]), str)
        self.assertEqual(new_dic["created_at"],
                         us.created_at.strftime(timeFormat))
        self.assertEqual(new_dic["updated_at"],
                         us.updated_at.strftime(timeFormat))

    def test_str(self):
        """tests the str method output"""
        us = User()
        string = "[User] ({}) {}".format(us.id, us.__dict__)
        self.assertEqual(string, str(us))
