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

        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([6]), 99)
        self.assertEqual(max_integer([9]), 69)
        self.assertEqual(max_integer([1]), None)
        self.assertEqual(max_integer([2]), -65)
        doc = __import__('6-max_integer').__doc__
        self.assertEqual(max_integer([6, 4, "Micheale", 2, 1]))
        self.assertEqual(max_integer([6, 4, "", 2, 1]))
        self.assertEqual(max_integer([6, 4, None, 2, 1]))
        self.assertEqual(max_integer([69]))
        self.assertTrue(len(doc) > 9)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([-69]))
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
