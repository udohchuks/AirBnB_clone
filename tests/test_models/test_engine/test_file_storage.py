#!/usr/bin/python3
"""
Test File Storage
"""
import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class TestFileStorage(unittest.TestCase):
    """Test File Storage
    """

    def setUp(self):
        """SetUp Class"""
        self.storage = FileStorage()
        self.storage.reload()

        self.amenity = Amenity()
        self.amenity.name = "Wi-Fi"
        self.amenity.save()

        self.place = Place()
        self.place.city_id = "city123"
        self.place.user_id = "user789"
        self.place.name = "Cozy Cabin"
        self.place.description = "A beautiful"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = ["amenity1"]
        self.place.save()

        self.city = City()
        self.city.state_id = "state789"
        self.city.name = "Los Angeles"
        self.city.save()

        self.user = User()
        self.user.email = "test@example.com"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.save()

        self.review = Review()
        self.review.place_id = "place123"
        self.review.user_id = "user456"
        self.review.text = "Great place!"
        self.review.save()

        self.state = State()
        self.state.name = "California"
        self.state.save()

        self.base = BaseModel()
        self.base.number = 90
        self.base.name = "Test"
        self.base.save()

    def test_reload_base_model(self):
        """Test Reload"""
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if obj.to_dict()["__class__"] == "BaseModel":
                self.assertEqual(obj.to_dict()["name"], "Test")
                self.assertEqual(obj.to_dict()["number"], 90)

    def test_reload_user(self):
        """Test Reload for User"""
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if isinstance(obj, User):
                self.assertEqual(obj.to_dict()["email"], "test@example.com")
                self.assertEqual(obj.to_dict()["first_name"], "John")
                self.assertEqual(obj.to_dict()["last_name"], "Doe")

    def test_reload_review(self):
        """Test Reload for Review"""
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if isinstance(obj, Review):
                self.assertEqual(obj.to_dict()["place_id"], "place123")
                self.assertEqual(obj.to_dict()["user_id"], "user456")
                self.assertEqual(obj.to_dict()["text"], "Great place!")

    def test_reload_state(self):
        """Test Reload for State"""
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if isinstance(obj, State):
                self.assertEqual(obj.to_dict()["name"], "California")

    def test_reload_city(self):
        """Test Reload for City"""
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if isinstance(obj, City):
                self.assertEqual(obj.to_dict()["state_id"], "state789")
                self.assertEqual(obj.to_dict()["name"], "Los Angeles")

    def test_reload_amenity(self):
        """Test Reload for Amenity"""
        self.amenity.save()
        all_objs = self.storage.all()
        self.storage.reload()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if isinstance(obj, Amenity):
                self.assertEqual(getattr(obj, "name"), "Wi-Fi")

    def test_reload_place(self):
        """Test Reload for Place"""
        self.place.save()
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if isinstance(obj, Place):
                self.assertEqual(obj.to_dict()["city_id"], "city123")
                self.assertEqual(obj.to_dict()["user_id"], "user789")
                self.assertEqual(obj.to_dict()["name"], "Cozy Cabin")
                self.assertEqual(obj.to_dict()["description"], "A beautiful")
                self.assertEqual(obj.to_dict()["number_rooms"], 2)
                self.assertEqual(obj.to_dict()["number_bathrooms"], 1)
                self.assertEqual(obj.to_dict()["max_guest"], 4)
                self.assertEqual(obj.to_dict()["price_by_night"], 100)
                self.assertEqual(obj.to_dict()["latitude"], 37.7749)
                self.assertEqual(obj.to_dict()["longitude"], -122.4194)
                self.assertEqual(obj.to_dict()["amenity_ids"], ["amenity1"])


if __name__ == '__main__':
    unittest.main()
