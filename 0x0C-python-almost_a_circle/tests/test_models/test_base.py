#!/usr/bin/python3
""" This module will be used for unittesting."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        b0 = Base(30)
        self.assertEqual(b0.id, 30)
        b1 = Base(76)
        self.assertEqual(b1.id, 76)
        b2 = Base(2)
        self.assertEqual(b2.id, 2)
        b3 = Base(45)
        self.assertEqual(b3.id, 45)
        b4 = Base(1)
        self.assertEqual(b4.id, 1)
        Base._Base__nb_objects = 0

    def test_no_argument(self):
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)
