#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            if all(isinstance(i, str) for i in attrs):
                return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
