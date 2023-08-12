#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructorr"""
        super().__init__(*args, **kwargs)
