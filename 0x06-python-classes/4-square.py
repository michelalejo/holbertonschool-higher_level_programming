#!/usr/bin/python3
class Square():
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size ** 2

    @size.setter
    def size(self, size_s):
        if type(size_s) != int:
            raise TypeError("size must be an integer")
        if size_s < 0:
            raise ValueError("size must be >= 0")
        self.__size = size_s
