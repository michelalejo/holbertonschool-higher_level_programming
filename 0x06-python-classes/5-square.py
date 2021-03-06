#!/usr/bin/python3
class Square():
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size_s):
        if type(size_s) != int:
            raise TypeError("size must be an integer")
        if size_s < 0:
            raise ValueError("size must be >= 0")
        self.__size = size_s

    def my_print(self):
        size = self.__size
        if size == 0:
            print("")
            return
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
