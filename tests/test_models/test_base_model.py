#!/usr/bin/python3
"""BaseModel Test"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class BaseTest(unittest.TestCase):
    """BaseModel test"""
    def setUp(self):
        """Initialize Basemodel"""
        self.model = BaseModel()

    def test_id_is_a_string(self):
        """Test Id Is a string
        """
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """Test created_at is datetime
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test updated_at is datetime
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_upadates_update_at(self):
        """Tesd save() updates update_at
        """
        original_update_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_update_at, self.model.updated_at)

    def test_to_dict_contains_classname(self):
        """test whether to_dict contain classname
        """
        model_dict = self.model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_to_dict_contain_created_at(self):
        """Test to_dict contain created_at
        """
        model_dict = self.model.to_dict()
        self.assertIn("created_at", model_dict)
        self.assertIsInstance(model_dict['created_at'], str)

    def test_to_dict_contain_updated_at(self):
        """Test to_dict contain updated_at
        """
        model_dict = self.model.to_dict()
        self.assertIn("updated_at", model_dict)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_contain_id(self):
        """Test to_dict contain id
        """
        model_dict = self.model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIsInstance(model_dict['id'], str)

    def test_str_representation(self):
        """Test string representation
        """
        model_str = str(self.model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(self.model.id, model_str)
        self.assertIn(str(self.model.__dict__), model_str)

    def test_inequality(self):
        """Test Equality of two classes"""
        model = BaseModel()
        model.number = 89
        model.name = "My_model"
        model2 = BaseModel(**model.to_dict())
        print(" ")
        print(model2)
        print("----\n")
        print(model2)
        self.assertNotEqual(model, model2)


if __name__ == "__main__":
    unittest.main()
