#!/usr/bin/python3
"""
FileStorage Module
"""
import os
import json


class FileStorage:
    """
    File Storage Module
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Constructor for FileStorage"""
        pass

    def all(self):
        """Return FileStorage"""
        return FileStorage.__objects

    def new(self, obj):
        """set obj in __object"""
        cls_name = obj.__class__.__name__
        FileStorage\
            .__objects["{}.{}".format(cls_name, obj.id)] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to json
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the json file if it exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                return FileStorage.__objects
