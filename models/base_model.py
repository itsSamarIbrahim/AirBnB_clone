#!/usr/bin/python3

import uuid
from datetime import datetime
from models.storage import storage


class BaseModel:
    """
    A class defining common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)

            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return string representation of BaseModel instance.
        """
        return "[{}] \
({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
