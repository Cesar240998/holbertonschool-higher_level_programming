#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    def test_Id_positive(self):
        """Testing for positive Base class ID
        """
        b1 = Base(2)
        self.assertEqual(b1.id, 2)
        b2 = Base(7)
        self.assertEqual(b2.id, 7)

    def test_Id_negative(self):
        """Testing for negative Base class ID
        """
        b1 = Base(-20)
        self.assertEqual(b1.id, -20)
        b2 = Base(-5)
        self.assertEqual(b2.id, -5)

    def test_Id_as_none(self):
        """Test for None Base Class ID
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_string_id(self):
        """Test Id as string
        """
        b1 = Base("Messi")
        self.assertEqual(b1.id, "Messi")
        b2 = Base("Cris")
        self.assertEqual(b2.id, "Cris")
