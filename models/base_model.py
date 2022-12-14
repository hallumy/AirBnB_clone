#!/usr/bin/python3
"""Base Model Module is a module in charge
of establishing a reference Base Model for
classes of the HBNB project
"""

import uuid
from datetime import datetime
from uuid import uuid4
import models


timeformat = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """BaseModel class
    This  Base Model defines all common attributes
    It also Initializes, serializers and deserializes
    future instances.

    """

    def __init__(self, *args, **kwargs):
        """Initialization of the Base Model Instances"""
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, timeformat)
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def to_dict(self):
        """An instance that returns a new dictionary containing
        all keys of __dict__
        """
        class_detail = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                class_detail[key] = item

        class_detail = self.__dict__.copy()
        class_detail['__class__'] = self.__class__.__name__
        class_detail['created_at'] = self.created_at.isoformat()
        class_detail['updated_at'] = self.updated_at.isoformat()
        return class_detail

    def __str__(self):
        """Representation of the class for the user"""

        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates the public instance"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
