#!/usr/bin/python3

"""
FileStorage Module
process -> <class 'BaseModel'> -> to_dict() -> <class 'dict'>
-> JSON dump -> <class 'str'> -> FILE -> <class 'str'>
-> JSON load -> <class 'dict'> -> <class 'BaseModel'>
"""

import os
import json
from models.base_model import BaseModel as BM
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns The self.__objects"""
        return self.__objects

    def new(self, obj):
        """Create a dictionary in self.__object
        key: value
            key: <class name>.<class id>
            value: is the object (__str__)
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves in the file.json
        form:
            key:obj.to_dict()
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Loads the json data back into the self.__objects
           Why:
                Because when ever we rerun our program our
                data in __object is lost
            Data in json is of the form:
                key:obj.to_dict()
            So we must convert back the obj.to_dict() to an obj
            by using BaseModel(**value[i.e, obj.to_dict()])
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                loaded_objs = json.load(f)
                for key, value in loaded_objs.items():
                    self.__objects[key] = BM(**value)
                    class_name = value['__class__']
                    if class_name == 'User':
                        instance = User(**value)
                    else:
                        instance = globals()[class_name](**value)
                    self.__objects[key] = instance
                else:
                    return
