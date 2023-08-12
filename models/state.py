#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = ""
