#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Programt Unittest for max_integer
    test max_integer
    Return: none"""

    def cases(self):
        """Programt Unittest for max_integer
        test max_integer
        Return: none"""

        self.assertEqual(max_integer([4]), 9)
        self.assertEqual(max_integer([0, 0]), 0)
        doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(doc) > 1)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([2]))
        self.assertEqual(max_integer([1, 2, "Hello", 4, 5]))
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
