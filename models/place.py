#!/usr/bin/python3
"""
Place module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class

    Attr:
        city_id (str): City id
        user_id (str): User id
        name (str): Place
        description (str): Description of place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Max guests at a time
        price_by_night (int): Price/night
        latitude (float): Latitude
        longitude (float): Longitude
        amenity_ids (list): Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
