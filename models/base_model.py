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
        # self.__dict__ = self.to_dict().copy()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for key, val in kwargs.items():
            if key != '__class__':
                if key == 'created_at' or key == 'updated_at':
                    new_val = datetime.fromisoformat(val)
                    self.__dict__[key] = new_val
                else:
                    self.__dict__[key] = val


    def __str__(self):
        # keys_to_remove = ['stdin', 'stdout', 'cmdqueue', 'completekey']
        #
        # # Remove unwanted keys
        # for key in keys_to_remove:
        #     self.__dict__.pop(key, None)
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

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
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat(),
        }
        # if not hasattr(self, '__class__'):
        #     self.__dict__['__class__'] = self.__class__.__name__

        # result_dict['updated_at'] = self.updated_at.isoformat()
        # if not hasattr(self, 'id'):
        #     self.id = str(uuid.uuid4())
        # result_dict['id'] = self.id
        # if not hasattr(self, 'created_at'):
        #     self.created_at = datetime.now()
        # result_dict['created_at'] = self.updated_at.isoformat()

        # # Include dynamically added attributes
        # for key, value in self.__dict__.items():
        #     if key not in result_dict and value is not None:
        #         result_dict[key] = value

        return result_dict
