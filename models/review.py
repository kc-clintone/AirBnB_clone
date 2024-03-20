#!/usr/bin/python3
"""
Review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class

    Attr:
        place_id (str): Place id
        user_id (str): User id
        text (str): content of review
    """
    place_id = ""
    user_id = ""
    text = ""
