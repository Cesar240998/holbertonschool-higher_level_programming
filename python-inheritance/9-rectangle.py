#!/usr/bin/python3
"""base_geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle based in BaseGeometry
    """
    def __init__(self, width, height):
        """Constructor of Retangle"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height

    def area(self):
        """Method that calculates area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Magic method to return rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
