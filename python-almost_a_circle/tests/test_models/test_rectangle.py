#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from io import StringIO
import sys
import os
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    """A class for test Rectangle
    """
    def test_Rectangle_arguments_exist(self):
        """Tests main attributes of rectangle
        """
        r1 = Rectangle(1, 2)
        self.assertEqual((r1.width, r1.height), (1, 2))

    def test_Rectangle_all_arguments(self):
        """Tests all attributes
        """
        r1 = Rectangle(5, 1, 0, 0, 4)
        r2 = Rectangle(12, 10, 0, 0, 10)
        self.assertEqual(r1.id, 4)
        self.assertEqual(r2.id, 10)

    def test_Rectangle_two_arguments(self):
        """Tests two arguments
        """
        r1 = Rectangle(1, 4)
        r2 = Rectangle(7, 11)
        r1.id = 5
        self.assertEqual(r1.id, 5)
        r2.id = 13
        self.assertEqual(r2.id, 13)


class Test_Rectangle_Attributes_Methods(unittest.TestCase):
    def test_Rectangle_str(self):
        """Tests attributes str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, "4")

    def test_Rectangle_negative(self):
        """Tests attributes in negative
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)

    def test_Rectangle_with_zero(self):
        """Tests zero in attributes
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 1)

    def test_area(self):
        """Test area
        """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)
        r1.width = 3
        self.assertEqual(r1.area(), 6)

    def test_Rectangle_str__exist(self):
        """Test function __str__
        """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (5) 3/4 - 1/2')

    def test_Rectangle_display(self):
        """Test function display
        """
        r1 = Rectangle(2, 3, 2, 2)
        prints = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), prints)

    def test_Rectangle_display1(self):
        r2 = Rectangle(1, 2, 1)
        prints = " #\n #\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), prints)

    def test_Rectangle_display2(self):
        r3 = Rectangle(1, 2)
        prints = "#\n#\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r3.display()
            self.assertEqual(fake_out.getvalue(), prints)

    def test_dict(self):
        """Test to dictionary function
        """
        r1 = Rectangle(10, 2, 1, 9, 9)
        r1_dict = r1.to_dictionary()
        d = {'x': 1, 'y': 9, 'id': 9, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dict, d)

    def test_update(self):
        """Test for public method update.
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test Update kwargs
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.id = 1
        r1.update(height=1)
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/1')
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), '[Rectangle] (1) 2/10 - 1/1')
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), '[Rectangle] (89) 3/1 - 2/1')
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')
