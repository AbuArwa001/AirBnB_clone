#!/usr/bin/python3
"""
MODULE: User Management Module

This module provides functionality for handling users.

Classes:
    User: Represents a user entity inheriting from BaseModel.

"""

from .base_model import BaseModel


class User(BaseModel):
    """
    User class representing a user entity.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Methods:
        __init__: Initializes a
        User instance with optional email, password, first name, and last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(
        self,
        *args,
        **kwargs
    ):
        """
        Initializes a User instance.

        Args:
            email (str, optional): The email address of the user.
            password (str, optional): The password of the user.
            first_name (str, optional): The first name of the user.
            last_name (str, optional): The last name of the user.
            *args: Variable length argument
                list passed to the superclass constructor.
            **kwargs: Arbitrary keyword arguments
                passed to the superclass constructor.
        """
        super().__init__(*args, **kwargs)
