#!/usr/bin/python3
"""module for AirBnB Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class attributes"""

    place_id = ""
    user_id = ""
    text = ""
