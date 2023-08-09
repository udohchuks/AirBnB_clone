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

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
            Args: args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
            Attributes:
                id: unique id generated
                created_at: creation date
                updated_at: updated date
         """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()

    def __str__(self):
        """
            __str___ of class
        """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

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

