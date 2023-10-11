# !/usr/bin/python3
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            obj_dict = {key: value.to_dict()
                        for key, value in FileStorage.__objects.items()}
            json.dump(obj_dict, file)

 #######################

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                FileStorage.__objects = obj_dict
                # for key, value in obj_dict.items():
                    # FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
           
