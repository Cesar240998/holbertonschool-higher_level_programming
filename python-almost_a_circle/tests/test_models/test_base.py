#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    def test_Base_Id(self):
        """This method creates a id secuential
        """
        b1 = Base(5)
        b2 = Base(12)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 12)

    def test_Base_Empty(self):
        """This method creates a id Empty
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_Base_Negative(self):
        """This method creates a id Negative
        """
        b1 = Base(-5)
        b2 = Base(-13)
        self.assertEqual(b1.id, -5)
        self.assertEqual(b2.id, -13)

    def test_Base_to_json_string_None(self):
        """This method validates a parameter None
        """
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')

    def test_Base_to_json_string_empty(self):
        """This method validates a parameter Empty
        """
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')
