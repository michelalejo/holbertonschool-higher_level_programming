#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry.
width and height objects.
Return: NULL
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry.
    width and height objects.
    Return: NULL"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[{}] {:d}/{:d}".format(type(self).__name__, self.__width,
                                       self.__height)
