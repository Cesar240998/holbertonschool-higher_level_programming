#!/usr/bin/python3
"""
Test differents behaviors of the Base class
"""
import unittest
import pycodestyle
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_Base_Id_positive(self):
        """This methods create a id secuential"""
        b1 = Base(30)
        self.assertEqual(b1.id, 30)
        b2 = Base(100)
        self.assertEqual(b2.id, 100)

    def test_Base_Empty(self):
        """This methods create a id Empty"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_Base_Id_Negative(self):
        """This methods create a id Negative"""
        b1 = Base(-20)
        self.assertEqual(b1.id, -20)
        b2 = Base(-7)
        self.assertEqual(b2.id, -7)
