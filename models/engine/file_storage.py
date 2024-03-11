#!/usr/bin/python3
"""FileStorage"""
import datetime, json, os

class FileStorage:

    """File/data storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns __objects"""
        return FileStorage.__objects

    def new(self, object):
        """Creates new object"""
        k = "{}.{}".format(type(object).__name__, object.id)
        FileStorage.__objects[k] = object

    def save(self):
        """Serializes the __objects dict to a JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            data = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(data, f)

    def classes(self):
        """Returns a dictionary"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place
        from models.state import State
        from models.user import User
        from models.city import City

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Persists stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            objd = json.load(f)
            objd = {key: self.classes()[value["__class__"]](**value)
                        for key, value in objd.items()}
            FileStorage.__objects = objd

    def attributes(self):
        """Returns attributes"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "f_name": str,
                      "s_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
