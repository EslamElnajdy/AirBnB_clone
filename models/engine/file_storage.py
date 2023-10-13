# !/usr/bin/python3
""" FileStorage module """
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    this class for storing and reloading data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        uses to return data((objects))
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        uses to make key with the name class and id
            then store the object as a value to key 
                in __objects.
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        uses to save the __objects in json file
        """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            obj_dict = {key: value.to_dict()
                        for key, value in FileStorage.__objects.items()}
            json.dump(obj_dict, file, indent=4)

 #######################

    def reload(self):
        """
        uses to reload the stored data 
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                FileStorage.__objects = obj_dict
                for key, value in obj_dict.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass

    def classes(self):
        """returns the class names in dict"""
        classes = {
            "BaseModel": BaseModel,
            "User": User
        }
        return classes
           
