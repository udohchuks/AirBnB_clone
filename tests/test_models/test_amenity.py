#!/usr/bin/python3
"""Test User Module"""
import unittest
from models.amenity import Amenity
from datetime import datetime
import models


class TestUser(unittest.TestCase):
    """Test User
    """

    def setUp(self):
        """SetUp"""
        self.user = Amenity()

    def test_attributes_existence(self):
        """ Test existence of attribute"""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_instance_creation(self):
        """Test Creation of attribute"""
        self.assertIsInstance(self.user, Amenity)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict_method(self):
        """Test To dict"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)

    def test_save_method(self):
        """Test save method"""
        prev_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(prev_updated_at, self.user.updated_at)

    def test_str_representation(self):
        """Test String Representation"""
        expected_str = \
            "[Amenity] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)


if __name__ == "__main__":
    unittest.main()
