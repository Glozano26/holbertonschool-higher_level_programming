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

    @staticmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        json_list = []
        if list_objs is not None:
            json_str = Base.to_json_string(cls, list_objs)
            json_file = open("cls.__name__", "w")
            json_file.write(json_str)
            json_file.close()
