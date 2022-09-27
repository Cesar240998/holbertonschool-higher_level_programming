#!/usr/bin/python3
"""
Create a Class Rectangle with:
- width, height private propreties
- getters & setters.
"""


class Rectangle:
    """Class - Rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor of a Square with the size and position"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter of the private attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for the size private attribute"""
        if (type(value) is not int):
            raise (TypeError("width must be an integer"))
        elif (value < 0):
            raise (ValueError("width must be >= 0"))
        else:
            self.__width = value
    
    @property
    def height(self):
        """Getter of the private attribute width"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for the size private attribute"""
        if (type(value) is not int):
            raise (TypeError("height must be an integer"))
        elif (value < 0):
            raise (ValueError("height must be >= 0"))
        else:
            self.__height = value
