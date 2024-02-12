#!/usr/bin/python3
"""
Module that imports  cmd module:
    console Starting point
"""
import cmd
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """
    Base model class
    Args:
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
        to_dict: converts to dictionary
        save: updates rime saved
    """

    def __init__(self, *args, **kwargs):
        """INITIALIZES CLASS BASEMODEL"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if not kwargs:
            self.__dict__["__class__"] = self.__class__.__name__
            # self.id = "1"
            storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    new_val = datetime.fromisoformat(val)
                    self.__dict__[key] = new_val
                else:
                    self.__dict__[key] = val

    def __str__(self):
        """Returns string representation of a class"""
        # dict_copy = self.__dict__.copy()
        # del dict_copy["__class__"]
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves and updates class"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing the attributes of the instance.

        This method creates a dictionary representation of the instance,
        including the common attributes 'id', 'x', and 'y'. Depending on
        the instance type (either a Rectangle or a Square), additional
        attributes such as 'width' and 'height' or 'size' are included in
        the dictionary.
        """
        result_dict = {}
        for attr_name, attr_value in self.__dict__.items():
            if attr_name == "created_at" or attr_name == "updated_at":
                # print(attr_value)
                val = attr_value.isoformat()
                result_dict[attr_name] = val
            else:
                result_dict[attr_name] = attr_value
        return result_dict
