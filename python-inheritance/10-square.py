#!/usr/bin/python3
"""base_geometry
"""


Rectangle = __import__('9-base_geometry').Rectangle


class Square(Rectangle):
    """
    Class square based in rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method that calculates area of square
        """
        return self.__size * self.__size
