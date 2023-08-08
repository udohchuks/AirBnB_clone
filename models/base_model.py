#!/usr/bin/python3

"""
    Module models.BaseModel
    This module contain the BaseModel
"""
import sys
import uuid
from datetime import datetime


class BaseModel:
    """
        The Base Model from which all other model will inherit
        It contains all common attributes
    """

    def __init__(self):
        """
            Constructor for BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """
            __str___ of class
        """ 
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Update updated_at
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Return: A new dict containing all self.__dict__
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.__dict__["updated_at"].isoformat()
        new_dict["created_at"] = self.__dict__["created_at"].isoformat()

        return new_dict

mymodel = BaseModel()
mymodel.number = 90
mymodel.name = "John"
print(mymodel)
mymodel.save()
print("\n")
print(mymodel)
print("\n")
my_model_json = mymodel.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))