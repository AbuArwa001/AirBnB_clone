

"""
    MODULE to handlee users
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    User class

    Attributes: email, password, first_name
                last_name

    """

    def __init__(self, email=None, password=None, first_name=None, last_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name

