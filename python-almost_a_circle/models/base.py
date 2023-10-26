#!/usr/bin/python3
"""first class Base"""
import json


class Base:
    """This class will be the “base” of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON is one of the standard formats
        for sharing data representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            my_dict = json.dumps(list_dictionaries)
            return my_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file method that writes the json string representation of
        list_obts to a file.

        Args:
            list_objs ([list of objects]): list of cls instances
        """
        list_dicts_python = []
        class_name = cls.__name__ + ".json"
        if list_objs is not None:
            for lst in list_objs:
                list_dicts_python.append(lst.to_dictionary())
        with open(class_name, "w+", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(list_dicts_python))

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            my_json = json.loads(json_string)
            return my_json
