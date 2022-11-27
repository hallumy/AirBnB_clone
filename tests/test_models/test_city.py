#!/usr/bin/python3
"""
To test the City class
"""
from datetime import datetime
import inspect
from models.base_model import BaseModel
import pep8
from models import city
import unittest
City = city.City


class testCity(unittest.TestCase):
    """Tests the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_fn = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test conformity to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test the conformity to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for docstrings in City methods"""
        for func in self.city_fn:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} methd needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} methd needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Test the City"""
    def test_is_subclass(self):
        """Test a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        city = City()
        new_dic = city.to_dict()
        self.assertEqual(type(new_dic), dict)
        for attr in city.__dict__:
            self.assertTrue(attr in new_dic)
            self.assertTrue("__class__" in new_dic)

    def test_to_dict_values(self):
        """test that values in dict"""
        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        new_dic = city.to_dict()
        self.assertEqual(new_dic["__class__"], "City")
        self.assertEqual(type(new_dic["created_at"]), str)
        self.assertEqual(type(new_dic["updated_at"]), str)
        self.assertEqual(new_dic["created_at"],
                         city.created_at.strftime(timeFormat))
        self.assertEqual(new_dic["updated_at"],
                         city.updated_at.strftime(timeFormat))

    def test_str(self):
        """test correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
