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
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
