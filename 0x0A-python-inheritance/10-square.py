#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry.
width and height objects.
Return: NULL
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Rectangle that inherits from BaseGeometry.
    width and height objects.
    Return: NULL"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
