#!/usr/bin/python3
"""
This program defines a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width attribute."""
        return self.__width

    @property
    def height(self):
        """Retrieves the heigth attribute."""
        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute."""
        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute."""
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of a Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with # char"""
        for k in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for l in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Informal representation of a Rectangle Instance"""
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
               .format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Updates rectangle attributes."""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle.
        """
        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
