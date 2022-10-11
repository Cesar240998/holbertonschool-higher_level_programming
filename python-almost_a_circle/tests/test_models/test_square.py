#!/usr/bin/python3
"""Unittest for class Square()
"""
import unittest
from io import StringIO
import sys
import os
import json
from unittest.mock import patch
from models.square import Square
from models.base import Base


class Test_Square(unittest.TestCase):
    """A class for test Square
    """
    def test_save_to_file(self):
        """Testing save_to_file"""
        test1 = Square(1, 1, 1, 1)
        test2 = Square(2, 2, 2, 2)
        li = [test1, test2]
        Square.save_to_file(l)
        with open("Square.json", "r") as file:
            ls = [test1.to_dictionary(), test2.to_dictionary()]
            self.assertEqual(json.dumps(ls), file.read())

    def test_empty_str(self):
        """pasing empy string"""
        li = []
        Square.save_to_file(l)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_none_str(self):
        """parsing none"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_load_f_file(self):
        """testing normal cases load file"""
        test1 = Square(2, 3, 4, 5)
        test2 = Square(7, 8, 9, 10)
        li = [test1, test2]
        Square.save_to_file(li)
        lo = Square.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        test1c = lo[0]
        test2c = lo[1]
        self.assertTrue(type(test1c) is Square)
        self.assertTrue(type(test2c) is Square)
        self.assertEqual(str(test1), str(test1c))
        self.assertEqual(str(test2), str(test2c))
        self.assertIsNot(test1, test1c)
        self.assertIsNot(test2, test2c)
        self.assertNotEqual(test1, test1c)
        self.assertNotEqual(test2, test2c)
