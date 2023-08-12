#!/usr/bin/python3
"""Test User Module"""
import unittest
from models.user import User
from datetime import datetime
import models


class TestUser(unittest.TestCase):
    """Test User
    """

    def setUp(self):
        """SetUp"""
        self.user = User()
        self.user.email = "email.com"
        self.user.password = "password"
        self.user.first_name = "mike"
        self.user.last_name = "john"

    def test_attributes_existence(self):
        """ Test existence of attribute"""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_instance_creation(self):
        """Test Creation of attribute"""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict_method(self):
        """Test To dict"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)

    def test_save_method(self):
        """Test save method"""
        prev_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(prev_updated_at, self.user.updated_at)

    def test_str_representation(self):
        """Test String Representation"""
        expected_str = \
            "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)


if __name__ == "__main__":
    unittest.main()
