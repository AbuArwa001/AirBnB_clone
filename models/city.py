"""
MODULE: City Module

This module provides functionality for handling city entities.

Classes:
    City: Represents a city entity inheriting from BaseModel.

"""

from .base_model import BaseModel


class City(BaseModel):
    """
    City class representing a city entity.

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.

    Methods:
        __init__: Initializes a City instance with an optional state ID and city name.

    """

    def __init__(self, state_id="", name="", *args, **kwargs):
        """
        Initializes a City instance.

        Args:
            state_id (str, optional): The ID of the state associated with the city.
            name (str, optional): The name of the city.
        """
        super().__init__(*args, **kwargs)
        self.state_id = state_id
        self.name = name
