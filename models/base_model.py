#!/usr/bin/python3
"""Base model: This is the base file for the project"""

import uuid
from models import storage
from datetime import datetime


class BaseModel:

    """Base class: All other classes will iherit this class"""

    def __init__(self, *args, **kwargs):
        """Initializing the instance attributes

        Args:
            - *args: The list of all args
            - **kwargs: A dictionary of the key/values args
        """

        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """This function returns a dict with all the keys/values of
        __dict__
        """

        this_dict = self.__dict__.copy()
        this_dict["__class__"] = type(self).__name__
        this_dict["created_at"] = this_dict["created_at"].isoformat()
        this_dict["updated_at"] = this_dict["updated_at"].isoformat()
        return this_dict

    def __str__(self):
        """This function returns the official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """This function will update the public instance attribute
           (updated_at)
        """

        self.updated_at = datetime.now()
        storage.save()
