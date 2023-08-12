#!/usr/bin/python3
"""
User Module
"""

from models.base_model import BaseModel

    
class User(BaseModel):
    """Inherits from Base Module"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
