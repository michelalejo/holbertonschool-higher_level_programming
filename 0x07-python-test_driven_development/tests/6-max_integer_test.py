#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Programt Unittest for max_integer
    test max_integer
    Return: none"""

    te_m = "'>' not supported between instances of 'str' and 'int'"

    def test_std_behavior(self):
        a = [1, 2, 3]
        self.assertEqual(max_integer(a), 3)

    def test_negatives(self):
        self.assertEqual(max_integer([-3, 5, -2]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([2.94, 1, 8.493]), 8.493)

    def test_multi_lists(self):
        a = [1, 2, 3]
        b = [1, 9, 3]
        c = [4, 2, 1]
        d = [a, b, c]
        self.assertEqual(max_integer(d), [4, 2, 1])

    def test_tuples(self):
        self.assertEqual(max_integer((8, 3, 12)), 12)

    def test_wrong_type(self):
        a = [1, 2, 'd', 3]
        with self.assertRaises(TypeError, msg=self.te_m):
            max_integer(a)
