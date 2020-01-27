#!/usr/bin/python3
"Square class"


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    "Square class"

    def __init__(self, size, x=0, y=0, id=None):
        "Rectangle init"
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        "Rectangle size"
        return self.__width

    @size.setter
    def size(self, value):
        "Rectangle size"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__height = value
        self.__width = value

    def __str__(self):
        "Rectangle __str__"
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        "Rectangle Update"
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.width = j
            elif i == 2:
                self.height = j
            elif i == 3:
                self.x = j
            elif i == 4:
                self.y = j

        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Rectangle Dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
