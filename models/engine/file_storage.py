#!/usr/bin/python3
"""
Serializing and deserializing module
"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.user import User


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary.
        """
        return  FileStorage.__objects

    def new(self, obj):
        """
         Sets an object in the __objects dictionary
        """
        obj_class_name = obj.__class__.__name__
        x = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[x] = obj

    def save(self):
        """
        Serializes the __objects dictionary into json format
        """
        changes = FileStorage.__objects
        object_dict = {}
        for x in changes.keys():
            object_dict[x] = changes[x].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        Deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    object_dict = json.load(file)
                    for i, j in object_dict.items():
                        class_name, object_id = i.split('.')
                        v_class = eval(class_name)
                        ins = v_class(**j)
                        FileStorage.__objects[i] = ins
                except Exception:
                    pass
