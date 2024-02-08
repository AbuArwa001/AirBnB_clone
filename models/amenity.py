"""
MODULE: Amenity Module

This module provides functionality for handling amenity entities.

Classes:
    Amenity: Represents an amenity entity inheriting from BaseModel.

"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class representing an amenity entity.

    Attributes:
        name (str): The name of the amenity.

    Methods:
        __init__: Initializes an Amenity instance with an optional name.

    """

    def __init__(self, name="", *args, **kwargs):
        """
        Initializes an Amenity instance.

        Args:
            name (str, optional): The name of the amenity.
        """
        super().__init__(*args, **kwargs)
        self.name = name
