#!/usr/bin/python3

"""
    Module models.BaseModel
    This module contain the BaseModel
"""

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class BaseModel:
    """
        The Base Model from which all other model will inherit
        It contains all common attributes
    """

    def __init__(self, *args, **kwargs):
        """
            Constructor for BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """Return: A new dict containing all self.__dict__
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.__dict__["updated_at"].isoformat()
        new_dict["created_at"] = self.__dict__["created_at"].isoformat()

        return new_dict
