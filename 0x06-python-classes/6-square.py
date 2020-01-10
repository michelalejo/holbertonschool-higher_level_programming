#!/usr/bin/python3
class Square():
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, SizeValue):
        if type(SizeValue) != int:
            raise TypeError("size must be an integer")
        if SizeValue < 0:
            raise ValueError("size must be >= 0")
        self.__size = SizeValue

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, PositionValue):
        if type(PositionValue) != tuple or len(PositionValue) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(val) != int for val in PositionValue):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in PositionValue):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = PositionValue

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for j in range(self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            [print("#", end="") for l in range(self.__size)]
            print("")
