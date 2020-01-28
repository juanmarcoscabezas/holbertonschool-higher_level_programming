#!/usr/bin/python3


"""
Unittest class base
"""

import unittest
from models.square import Square


class ClassSquareTest(unittest.TestCase):

    def setUp(self):
        rec = Square(1, 1)

    def test_00(self):
        """test success"""
        r = Square(1, 1)
        self.assertEqual(r.id, 62)

    def test_01(self):
        """test sucess"""
        r = Square(1, 1)
        self.assertEqual(r.id, 64)

    def test_02(self):
        """test height string"""
        with self.assertRaises(TypeError):
            Square(1, "Holberton")

    def test_03(self):
        """test height float"""
        with self.assertRaises(TypeError):
            Square(1, 1.4)

    def test_04(self):
        """test height negative"""
        with self.assertRaises(ValueError):
            Square(1, -3)

    def test_05(self):
        """test height None"""
        with self.assertRaises(TypeError):
            Square(1, None)

    def test_06(self):
        """test height dict"""
        with self.assertRaises(TypeError):
            Square(1, {'id': 7})

    def test_07(self):
        """test height list"""
        with self.assertRaises(TypeError):
            Square(1, [1, 2, 3])

    def test_e02(self):
        """test width string"""
        with self.assertRaises(TypeError):
            Square("Holberton", 1)

    def test_e03(self):
        """test width float"""
        with self.assertRaises(TypeError):
            Square(1.4, 1)

    def test_e04(self):
        """test width negative"""
        with self.assertRaises(ValueError):
            Square(-3, 1)

    def test_e05(self):
        """test width None"""
        with self.assertRaises(TypeError):
            Square(None, 1)

    def test_e06(self):
        """test width dict"""
        with self.assertRaises(TypeError):
            Square({'id': 7}, 1)

    def test_e07(self):
        """test width list"""
        with self.assertRaises(TypeError):
            Square([1, 2, 3], 1)

    def test_08(self):
        """test width"""
        r = Square(1, 2)
        self.assertEqual(r.width, 1)

    def test_09(self):
        """test height"""
        r = Square(1, 2)
        self.assertEqual(r.height, 2)

    def test_10(self):
        """test area"""
        r = Square(3, 2)
        self.assertEqual(r.area(), 6)

    def test_11(self):
        """test set width"""
        r = Square(1, 2)
        r.width = 4
        self.assertEqual(r.width, 4)

    def test_12(self):
        """test set height"""
        r = Square(1, 2)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_13(self):
        """test display"""
        r = Square(1, 1)
        self.assertEqual(r.display(), None)

    def test_e14(self):
        """test x"""
        with self.assertRaises(ValueError):
            r = Square(1, 1, -1, 1)

    def test_e15(self):
        """test y"""
        with self.assertRaises(ValueError):
            r = Square(1, 1, 1, -1)

    def test_e16(self):
        """test x"""
        with self.assertRaises(TypeError):
            r = Square(1, 1, None, 1)

    def test_e17(self):
        """test x"""
        with self.assertRaises(TypeError):
            r = Square(1, 1, 1, None)

    def test_e18(self):
        """test width"""
        with self.assertRaises(ValueError):
            r = Square(0, 1)

    def test_e19(self):
        """test height"""
        with self.assertRaises(ValueError):
            r = Square(1, 0)

    def test_14(self):
        """update 1"""
        r = Square(1, 1, 1, 1)
        r.update(2)
        self.assertEqual(r.id, 2)

    def test_15(self):
        """update 2"""
        r = Square(1, 1, 1, 1)
        r.update(2, 3)
        self.assertEqual(r.id, 2)
        self.assertEqual(r. width, 3)

    def test_16(self):
        """update 2"""
        r = Square(1, 1, 1, 1)
        r.update(2, 3, 4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_17(self):
        """update 2"""
        r = Square(1, 1, 1, 1)
        r.update(2, 3, 4, 5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)

    def test_18(self):
        """update 2"""
        r = Square(1, 1, 1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_19(self):
        """test x getter"""
        r = Square(1, 1, 1, 1)
        r.x = 10
        self.assertEqual(r.x, 10)

    def test_20(self):
        """test y getter"""
        r = Square(1, 1, 1, 1)
        r.y = 10
        self.assertEqual(r.y, 10)

    def test_21(self):
        """test docstring"""
        self.assertIsNotNone(Square.__doc__)
