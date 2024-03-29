#!/usr/bin/python3
"""
MODULE: Place Management Module

This module provides functionality for handling place entities.

Classes:
    Place: Represents a place entity inheriting from BaseModel.

"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    Place class representing a place entity.

    Attributes:
        city_id (str): The ID of the city associated with the place.
        user_id (str): The ID of the user associated with the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (float): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of IDs of
            amenities associated with the place.

    Methods:
        __init__: Initializes a Place instance with optional parameters.

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []

    def __init__(
        self,
        *args,
        **kwargs
    ):
        """
        Initializes a Place instance.

        Args:
            city_id (str, optional):
                The ID of the city associated with the place.
            user_id (str, optional):
                The ID of the user associated with the place.
            name (str, optional): The name of the place.
            description (str, optional): The description of the place.
            number_rooms (int, optional): The number of rooms in the place.
            number_bathrooms (int, optional):
                The number of bathrooms in the place.
            max_guest (int, optional):
                The maximum number of guests allowed in the place.
            price_by_night (float, optional): The price per night for the place
            latitude (float, optional): The latitude coordinate of the place.
            longitude (float, optional): The longitude coordinate of the place.
            amenity_ids (list, optional):
                A list of IDs of amenities associated with the place.
            *args: Variable length argument
                list passed to the superclass constructor.
            **kwargs: Arbitrary keyword arguments
                passed to the superclass constructor.
        """
        super().__init__(*args, **kwargs)
