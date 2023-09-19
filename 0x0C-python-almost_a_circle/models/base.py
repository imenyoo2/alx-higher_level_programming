#!/usr/bin/python3
"""defines Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representation"""
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json representation"""
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string([x.to_dictionary() for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """import from json file"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates new instance of cls with attributes set to dictionary"""
        buffer = cls(1, 1)
        buffer.update(**dictionary)
        return buffer

    @classmethod
    def load_from_file(cls):
        """load from json file"""
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                list = cls.from_json_string(f.read())
                for i in range(len(list)):
                    list[i] = cls.create(**list[i])
                return list
        except FileNotFoundError:
            return []
