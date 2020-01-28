#!/usr/bin/python3
"Square class"


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
        return (self.__width)

    @size.setter
    def size(self, value):
        "Rectangle size"
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__height = value
        self.__width = value

    def __str__(self):
        "Rectangle __str__"
        return("[Square] ({}) {}/{} - {}".format
               (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        "Rectangle Update"
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.size = j
            elif i == 2:
                self.x = j
            elif i == 3:
                self.y = j
        if args is None or len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Rectangle Dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
