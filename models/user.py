#!/usr/bin/python3
"""
User Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from Base Module"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
