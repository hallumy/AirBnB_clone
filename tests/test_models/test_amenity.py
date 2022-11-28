#!usr/bin/python3
"""
To test Amenity
"""

from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8
import unittest
import inspect
Amenity = amenity.Amenity


class test_amenity(unittest.TestCase):
    """Tests the  Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up class for the doc_tests"""
        cls.amenity_fn = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Tests the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Tests the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methds"""
        for func in self.amenity_fn:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attr name, and empty string"""

        self.assertTrue(hasattr(self.new_inst, "name"))

    def test_to_dict_on_Amenity(self):
        """test to_dict instance has _class_ key"""

        new_dict = self.new_inst.to_dict()
        self.assertEqual(new_dict['__class__'], 'Amenity')
        self.assertEqual(str(type(new_dict['created_at'])),
                         "< class 'str' > ")
        self.assertEqual(str(type(new_dict['updated_at'])),
                         "< class 'str' > ")

    def test_to_dict_values(self):
        """test values in dict returned from to_dict"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        Am = Amenity()
        new_dict = self.Am.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict["created_at"]),
                         str)
        self.assertEqual(type(new_dict["updated_at"]),
                         str)
        self.assertEqual(new_dict["created_at"],
                         Am.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         Am.updated_at.strftime(t_format))

    def test_str(self):
        """test the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
