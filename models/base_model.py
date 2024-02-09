#!/usr/bin/python3
"""

"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    """
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] (self.id) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy


# if __name__ == "__main__":
#     base_model = BaseModel()
#     print(base_model)
#     print()
#     base_model.save()
#     print(base_model)
#     print()
#     print(base_model.to_dict())
