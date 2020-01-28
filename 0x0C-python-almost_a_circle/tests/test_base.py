#!/usr/bin/python3


"""
Unittest class base
"""

import unittest
from models.base import Base


class ClassBaseTest(unittest.TestCase):

    def setUp(self):
        base = Base()

    def test_00(self):
        """test no id"""
        base = Base()
        self.assertEqual(base.id, 2)

    def test_01(self):
        """test id number"""
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_02(self):
        """test id string"""
        base = Base("Holberton")
        self.assertEqual(base.id, "Holberton")

    def test_03(self):
        """test id float"""
        base = Base(1.4)
        self.assertEqual(base.id, 1.4)

    def test_04(self):
        """test id negative"""
        base = Base(-3)
        self.assertEqual(base.id, -3)

    def test_05(self):
        """test id None"""
        base = Base(None)
        self.assertEqual(base.id, 8)

    def test_06(self):
        """test id dict"""
        base = Base({'id': 7})
        self.assertEqual(base.id, {'id': 7})

    def test_04(self):
        """test id list"""
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])
