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
        self.assertEqual(r.id, 12)

    def test_01(self):
        """test sucess"""
        r = Rectangle(1, 1)
        self.assertEqual(r.id, 14)

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

    def test_07(self):
        """test height list"""
        with self.assertRaises(TypeError):
            Rectangle(1, [1, 2, 3])

    def test_e02(self):
        """test width string"""
        with self.assertRaises(TypeError):
            Rectangle("Holberton", 1)

    def test_e03(self):
        """test width float"""
        with self.assertRaises(TypeError):
            Rectangle(1.4, 1)

    def test_e04(self):
        """test width negative"""
        with self.assertRaises(ValueError):
            Rectangle(-3, 1)

    def test_e05(self):
        """test width None"""
        with self.assertRaises(TypeError):
            Rectangle(None, 1)

    def test_e06(self):
        """test width dict"""
        with self.assertRaises(TypeError):
            Rectangle({'id': 7}, 1)

    def test_e07(self):
        """test width list"""
        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3], 1)

    def test_08(self):
        """test width"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_09(self):
        """test height"""
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)

    def test_10(self):
        """test area"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_11(self):
        """test set width"""
        r = Rectangle(1, 2)
        r.width = 4
        self.assertEqual(r.width, 4)

    def test_12(self):
        """test set height"""
        r = Rectangle(1, 2)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_13(self):
        """test display"""
        r = Rectangle(1, 1)
        self.assertEqual(r.display(), None)

    def test_e14(self):
        """test x"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -1, 1)

    def test_e15(self):
        """test y"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, 1, -1)

    def test_e16(self):
        """test x"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, None, 1)

    def test_e17(self):
        """test x"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, None)

    def test_e18(self):
        """test width"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)

    def test_e19(self):
        """test height"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_14(self):
        """update 1"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2)
        self.assertEqual(r.id, 2)

    def test_15(self):
        """update 2"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2, 3)
        self.assertEqual(r.id, 2)
        self.assertEqual(r. width, 3)

    def test_16(self):
        """update 2"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2, 3, 4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_17(self):
        """update 2"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2, 3, 4, 5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)

    def test_18(self):
        """update 2"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_19(self):
        """test x getter"""
        r = Rectangle(1, 1, 1, 1)
        r.x = 10
        self.assertEqual(r.x, 10)

    def test_20(self):
        """test y getter"""
        r = Rectangle(1, 1, 1, 1)
        r.y = 10
        self.assertEqual(r.y, 10)

    def test_21(self):
        """test docstring"""
        self.assertIsNotNone(Rectangle.__doc__)
