"""
MODULE: Review Management Module

This module provides functionality for handling review entities.

Classes:
    Review: Represents a review entity inheriting from BaseModel.

"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class representing a review entity.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.

    Methods:
        __init__: Initializes a Review instance with optional parameters.

    """

    def __init__(self, place_id="", user_id="", text="",  *args, **kwargs):
        """
        Initializes a Review instance.

        Args:
            review_id (str, optional): The ID of the review.
            place_id (str, optional): The ID of the place associated with the review.
            user_id (str, optional): The ID of the user who wrote the review.
            text (str, optional): The content of the review.
            *args: Variable length argument list passed to the superclass constructor.
            **kwargs: Arbitrary keyword arguments passed to the superclass constructor.
        """
        super().__init__(*args, **kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
