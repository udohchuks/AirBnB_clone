#!/usr/bin/python3
"""
Test File Storage
"""
import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test File Storage
    """
    def setUp(self):
        """SetUp Class"""
        self.storage = FileStorage()
        self.storage.reload()
    
    def tearDown(self):
        """If File exist after each call of test remove file"""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)
    
    def test_reload(self):
        """Test Reload"""
        obj = BaseModel()
        obj.number = 90
        obj.name = "Test"
        obj.save()
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertEqual(obj.to_dict()["name"], "Test")
            self.assertEqual(obj.to_dict()["number"], 90)

if __name__ == '__main__':
    unittest.main()
