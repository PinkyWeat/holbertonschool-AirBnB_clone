#!/usr/bin/python3
"""Module User Class - Inherits from BaseModel"""
from models import BaseModel


class User(BaseModel):
    """User attributes & methods"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""