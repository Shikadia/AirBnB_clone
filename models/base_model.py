#!/usr/bin/python3
"""This defines a class for BaseModel"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The base model class"""
    def __init__(self, *args, **kwargs):
        """
        This initializies a new basemodel.

        Args:
            *args (tuple): Arbitrary positional arguments (Unused).
            **kwargs (dict): key value pair of attributes.
        """

        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.strptime(y, time_fmt)
                else:
                    self.__dict__[x] = y
        else:
            models.storage.new(self)

    def __str__(self):
        """
        retunrs the str representation in a specific format
        """
        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.update_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        """
        returns the dictionary conatining all keys value of the instance
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic
