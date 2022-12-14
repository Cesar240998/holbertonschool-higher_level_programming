#!/usr/bin/python3
"""
Create a Class Rectangle with:
- width, height private propreties
- getters & setters.
"""


class Rectangle:
    """Class - Rectangle"""

    # Public
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor of a Square with the size and position"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Method to get the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Method to get the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """
        Print() __str__ method funtion to return rectangle in char '#'
        """
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res

        for i in range(self.__height):
            for j in range(self.__width):
                res += str(self.print_symbol)
            if i != self.__height - 1:
                res += '\n'
        return res

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message for del
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a square of the size
        """
        height = size
        width = size
        return cls(height, width)
