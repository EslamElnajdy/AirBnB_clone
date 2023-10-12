# !/usr/bin/python3
""" FileStorage module """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            obj_dict = {}

            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()

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
                classes = self.classes()
                
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name in classes:
                        FileStorage.__objects[key] = classes[class_name](**value)
        except FileNotFoundError:
            pass

    def classes(self):
        """returns the class names in dict"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Review": Review,
            "State": State,
            "Amenity": Amenity,
            "Place": Place
        }
        return classes
           
