#!/usr/bin/python3
"""The base model: Blue print of all models"""

from datetime import datetime
import uuid


class BaseModel:
    """This is going to be the base class that all others will inherit"""
    def __init__(self, *args, **kwargs):
        """
        Args:
            - *args: positional args
            - **kwargs: keyword args
        Initializes the objects.
        """

        std_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs is not None and kwargs != {}:
            for x in kwargs:
                if x == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], std_format)
                elif x == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], std_format)
                else:
                    self.__dict__[x] = kwargs[x]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        save to local storage
        """
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """
         returns str representation
        """
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)

    def to_dict(self):
        """
        save key/value paira to __dict__
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict


if __name__ == "__main__":
    test_model = BaseModel()
    test_model.name = "test model"
    test_model.test_number = 89
    print(test_model)
    test_model.save()
    print(test_model)
    test_model_json_format = test_model.to_dict()
    print(test_model_json_format)
    print("____json version of test_model____")
    for i in test_model_json_format.keys():
        print("\t{}: ({}) - {}".format(i, type(test_model_json_format[i]),
              test_model_json_format[i]))
