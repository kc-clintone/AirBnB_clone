#!/usr/bin/python3
"""
City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class

    Attr:
        state_id (str): State id
        name (str): Name of city
    """
    state_id = ""
    name = ""
