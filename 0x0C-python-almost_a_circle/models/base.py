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
        """Base Staticmetohd"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
