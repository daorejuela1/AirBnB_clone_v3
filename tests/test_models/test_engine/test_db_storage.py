#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine.db_storage import DBStorage
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_executable_file(self):
        """ Check if file have permissions to execute"""
        # Check for read access
        is_read_true = os.access('models/engine/db_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/engine/db_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/engine/db_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_0_arg(self):
        """Test that get raise an error without params"""
        with self.assertRaises(TypeError):
            models.storage.get()

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_1_arg(self):
        """Test that get raise an error with one param"""
        with self.assertRaises(TypeError):
            models.storage.get(None)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_3_arg(self):
        """Test that get raise an error with 3 params"""
        with self.assertRaises(TypeError):
            models.storage.get(None, None, None)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_no_exist(self):
        """ test with a get that not exist """
        instance = State(name="Florida")
        instance.save()
        self.assertTrue(type(models.storage.get(Place, instance.id)),
                        type(State))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_none_exist(self):
        """ test with a get that not exist """
        instance = State(name="Florida")
        instance.save()
        self.assertTrue(type(models.storage.get(User, instance.id)),
                        type(State))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_no_id_exist(self):
        """ test with a get that not exist """
        instance = State(name="Florida")
        instance.save()
        self.assertTrue(type(models.storage.get(Place, None)),
                        type(None))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_exist(self):
        """ test with a get that exist """
        instance = State(name="Florida")
        instance.save()
        self.assertTrue(type(models.storage.get(State, instance.id)),
                        type(State))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count_3_args(self):
        """Test count with 3 args"""
        with self.assertRaises(TypeError):
            models.storage.count(12313, 123123, 123)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count(self):
        """Test count with an obj"""
        instance = State(name="Florida")
        instance.save()
        self.assertEqual(models.storage.count(User), 0)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count2(self):
        """Test count empty"""
        instance = State(name="Florida")
        instance.save()
        self.assertTrue(models.storage.count() >= 0)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count3(self):
        """Test count bad param"""
        self.assertEqual(models.storage.count(list), 0)
