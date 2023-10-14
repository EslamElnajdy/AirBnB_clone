#!/usr/bin/python3

"""base_model module"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel that defines all
        common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        initializes the instanes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        return a human-readable string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def __repr__(self):
        """
        repr
        """
        return self.__str__

    def save(self):
        """
        updates the public instance
            attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
