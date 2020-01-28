#!/usr/bin/python3
"Base class"
import json
import csv
from os import path


class Base:
    "Base class"
    __nb_objects = 0

    def __init__(self, id=None):
        "Base method"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        "Base Staticmetohd"
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        "Base Classmetohd"
        dic = []
        if list_objs:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(dic))
