#!/usr/bin/python3
"""Unittest for class Rectangle()
"""
import unittest
from io import StringIO
import sys
import os
import json
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

    def test_Rectangle_create(self):
        """Test method Create
        """
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(str(r1), '[Rectangle] (89) 0/0 - 1/1')

        r2 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(str(r2), '[Rectangle] (89) 0/0 - 1/1')

        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r3), '[Rectangle] (89) 0/0 - 1/2')

        r4 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r4), '[Rectangle] (89) 3/0 - 1/2')

        r5 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3,
                                 'y': 4})
        self.assertEqual(str(r5), '[Rectangle] (89) 3/4 - 1/2')

    def test_save_to_file(self):
        """These methods will test save_to_file
        """
        test1 = Rectangle(1, 1, 1, 1)
        test2 = Rectangle(2, 2, 2, 2)
        lista = [test1, test2]
        Rectangle.save_to_file(lista)
        with open("Rectangle.json", "r") as file:
            ls = [test1.to_dictionary(), test2.to_dictionary()]
            self.assertEqual(json.dumps(ls), file.read())

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            ls = []
            self.assertEqual(json.dumps(ls), file.read())

    def test_load_f_file(self):
        """testing normal cases load file
        """
        test1 = Rectangle(1, 2, 3, 4, 5)
        test2 = Rectangle(6, 7, 8, 9, 10)
        li = [test1, test2]
        Rectangle.save_to_file(li)
        lo = Rectangle.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        test1c = lo[0]
        test2c = lo[1]
        self.assertTrue(type(test1c) is Rectangle)
        self.assertTrue(type(test2c) is Rectangle)
        self.assertEqual(str(test1), str(test1c))
        self.assertEqual(str(test2), str(test2c))
        self.assertIsNot(test1, test1c)
        self.assertIsNot(test2, test2c)
        self.assertNotEqual(test1, test1c)
        self.assertNotEqual(test2, test2c)
