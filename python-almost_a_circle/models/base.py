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
        list_empty = []
        if json_string is not None:
            return json.loads(json_string)
        else:
            return list_empty

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance"""
        new_inst = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """File to instances"""
        list_ret = []
        class_name = cls.__name__ + ".json"
        with open(class_name, mode="r") as file:
            list_ret_print = cls.from_json_string(file.read())
            for objt in list_ret_print:
                list_ret.append(cls.create(**objt))
        return list_ret
