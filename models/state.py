#!/usr/bin/python3
"""
MODULE: State Module

This module provides functionality for handling state entities.

Classes:
    State: Represents a state entity inheriting from BaseModel.

"""

from .base_model import BaseModel


class State(BaseModel):
    """
    State class representing a state entity.

    Attributes:
        name (str): The name of the state.

    Methods:
        __init__: Initializes a State instance with an optional state name.

    """
    name = ""

    def __init__(self,  *args, **kwargs):
        """
        Initializes a State instance.

        Args:
            name (str, optional): The name of the state.
        """
        super().__init__(*args, **kwargs)
