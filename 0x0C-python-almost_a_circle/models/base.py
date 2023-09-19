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
        fstr = "[" + "{}, " * len(list_objs)
        fstr = fstr[:-2] + "]"
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(fstr.format(*[cls.to_json_string(x.to_dictionary()) for x in list_objs]))
