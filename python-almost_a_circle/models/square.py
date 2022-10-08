#!/usr/bin/python3
"""
This program defines a Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Returns formatted information display
        """
        return "({}) {}/{} - {}".format(self.id, self.x, self.y,
                                        self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """size needs to be an int
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates square attributes."""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()
