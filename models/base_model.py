import cmd
import uuid
from datetime import datetime

"""
Module that imports  cmd module:
    console Starting point
"""


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
        # Uncomment the following line if this class inherits from another class
        # super().__init__()
        # print(self.__dict__)
        # print(self.to_dict())
        self.__dict__ = self.to_dict().copy()
        del self.__dict__['__class__']
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    @property
    def updated_at(self):
        """
        Get the value of the 'updated_at' attribute.

        Returns:
            datetime: The value of the 'updated_at' attribute.
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """
        Set the value of the 'updated_at' attribute.

        Args:
            value (datetime): The new value for 'updated_at'.

        Raises:
            ValueError: If the provided value is not a datetime object.
        """
        if not isinstance(value, datetime):
            raise ValueError("Value must be a datetime object.")
        self._updated_at = value

    @property
    def id(self):
        """
        Get the value of the 'id' attribute.

        Returns:
            str: The value of the 'id' attribute.
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        Set the value of the 'id' attribute.

        Args:
            value (str): The new value for 'id'.

        Raises:
            ValueError: If the provided value is not a string.
        """
        if not isinstance(value, str):
            raise ValueError("Value must be a string.")
        self._id = value

    @property
    def created_at(self):
        """
        Get the value of the 'created_at' attribute.

        Returns:
            datetime: The value of the 'created_at' attribute.
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """
        Set the value of the 'created_at' attribute.

        Args:
            value (datetime): The new value for 'created_at'.

        Raises:
            ValueError: If the provided value is not a datetime object.
        """
        if not isinstance(value, datetime):
            raise ValueError("Value must be a datetime object.")
        self._created_at = value

    def __str__(self):
        # keys_to_remove = ['stdin', 'stdout', 'cmdqueue', 'completekey']
        #
        # # Remove unwanted keys
        # for key in keys_to_remove:
        #     self.__dict__.pop(key, None)
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

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
        result_dict = {
            'my_number': getattr(self, 'my_number', None),
            'name': getattr(self, 'name', None),
            '__class__': "None",
            # 'updated_at': self.updated_at.isoformat(),
            # 'id': self.id,
            # 'created_at': self.created_at.isoformat(),
        }
        if not hasattr(self, 'updated_at'):
            self.updated_at = datetime.now()

        result_dict['updated_at'] = self.updated_at.isoformat()
        if not hasattr(self, 'id'):
            self.id = str(uuid.uuid4())
        result_dict['id'] = self.id
        if not hasattr(self, 'created_at'):
            self.created_at = datetime.now()
        result_dict['created_at'] = self.updated_at.isoformat()

        # Include dynamically added attributes
        # for key, value in self.__dict__.items():
        #     if key not in result_dict and value is not None:
        #         result_dict[key] = value
        if isinstance(self, BaseModel):
            result_dict['__class__'] = self.__class__.__name__
        else:
            result_dict['__class__'] = "Base"

        return result_dict
