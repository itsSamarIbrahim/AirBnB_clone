#!/usr/bin/python3
"""
A class BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes.
    """

    def __init__(self, storage=None, *args, **kwargs):
        """
        Initialize BaseModel instance.
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid4)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            if storage:
                storage.new(self)
        self.storage = storage

    def __str__(self):
        """
        Return string representation of BaseModel instance.
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        if self.storage:
            self.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
