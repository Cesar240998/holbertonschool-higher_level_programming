#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testing Base
    """
    
    def tearDown(self):
        """Tears down obj count
        """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """Test instantiation
        """
        b1 = Base()
        b2 = Base(9)
        b3 = Base(9.5)
        b4 = Base(float('inf'))
        b5 = Base("string")
        b6 = Base(["list", 4, 2.5])
        b7 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 9)
        self.assertEqual(b3.id, 9.5)
        self.assertEqual(b4.id, float('inf'))
        self.assertEqual(b5.id, "string")
        self.assertEqual(b6.id, ["list", 4, 2.5])
        self.assertEqual(b7.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_to_json_string(self):
        """Testing to_json_string()
        """
        b1_1 = [{"hi": 1, "yo": "hol"}]
        b1_2 = [{"hello": 3}]
        b1_3 = None
        b1_4 = "a string"
        b1_5 = 123
        b1_6 = [[1, 2, 3]]
        b1_7 = []

        self.assertCountEqual(Base.to_json_string(b1_1),
                              '[{"hi": 1, "yo": "hol"}]')
        self.assertCountEqual(Base.to_json_string(b1_2), '[{"hello": 3}]')
        self.assertCountEqual(Base.to_json_string(b1_3), '[]')
        self.assertCountEqual(Base.to_json_string(b1_4), '"a string"')
        with self.assertRaises(TypeError):
            Base.to_json_string(b1_5)
        self.assertCountEqual(Base.to_json_string(b1_6), '[[1, 2, 3]]')
        self.assertCountEqual(Base.to_json_string(b1_7), '[]')
