#!/usr/bin/python3
"""base_geometry
"""


class BaseGeometry:
    """Contains a function area()
    """
    def area(self):
        """Function not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates `value`
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
