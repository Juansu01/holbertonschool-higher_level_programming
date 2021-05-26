#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-1, 2, 10, 8]), 10)
        self.assertAlmostEqual(max_integer([-1, 2, 5, 8]), 8)
        self.assertAlmostEqual(max_integer([10, 2, 5, 8]), 10)
        self.assertAlmostEqual(max_integer([-1, 2, 34, 5, 8]), 34)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertAlmostEqual(max_integer([3]), 3)
