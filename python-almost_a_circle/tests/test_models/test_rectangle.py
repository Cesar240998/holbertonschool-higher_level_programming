#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
import io
import sys
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    def test_Rectangle_arguments_exist(self):
        """This methods will be tested with all_arguments
        """
        r1 = Rectangle(1, 2)
        self.assertEqual((r1.width, r1.height), (1, 2))

    def test_Rectangle_all_arguments(self):
        """This methods will be tested with all_arguments
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(2, 10, 0, 0, 5)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r2.id, 5)

    def test_Rectangle_two_arguments(self):
        """This methods will be tested with two_arguments
        """
        r1 = Rectangle(13, 2)
        r2 = Rectangle(5, 4)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2.id = 2
        self.assertEqual(r2.id, 2)


class Test_Rectangle_validate_atributes(unittest.TestCase):
    def test_Rectangle_str(self):
        """This methods will be tested with str value
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")
