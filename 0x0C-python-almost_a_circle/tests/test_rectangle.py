#!/usr/bin/python3


"""
Unittest class base
"""

import unittest
from models.rectangle import Rectangle


class ClassRectangleTest(unittest.TestCase):

    def setUp(self):
        rec = Rectangle(1, 1)

    def test_00(self):
        """test success"""
        r = Rectangle(1, 1)
        self.assertEqual(r.id, 11)

    def test_01(self):
        """test sucess"""
        r = Rectangle(1, 1)
        self.assertEqual(r.id, 13)

    def test_02(self):
        """test height string"""
        with self.assertRaises(TypeError):
            Rectangle(1, "Holberton")

    def test_03(self):
        """test height float"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1.4)

    def test_04(self):
        """test height negative"""
        with self.assertRaises(ValueError):
            Rectangle(1, -3)

    def test_05(self):
        """test height None"""
        with self.assertRaises(TypeError):
            Rectangle(1, None)

    def test_06(self):
        """test height dict"""
        with self.assertRaises(TypeError):
            Rectangle(1, {'id': 7})

    def test_04(self):
        """test height list"""
        with self.assertRaises(TypeError):
            Rectangle(1, [1, 2, 3])
