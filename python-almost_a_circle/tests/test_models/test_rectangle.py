#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
import io
import sys
from models.rectangle import Rectangle


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


class Test_Rectangle_Attributes(unittest.TestCase):
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
        """Tests attributes in negative"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)
