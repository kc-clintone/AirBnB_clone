#!/usr/bin/python3
"""
User module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class: Handles user info
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
