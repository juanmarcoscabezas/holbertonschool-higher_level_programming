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

    def test_01(self):
        """test id number"""
        base = Base(1)

    def test_02(self):
        """test id string"""
        base = Base("Holberton")

    def test_03(self):
        """to_json_string"""
        base = Base()
        base.to_json_string([{'x': 10}])
