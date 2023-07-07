#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test case for max_integer"""

    def test_normal(self):
        """testing for positive testing"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "max at the end")
        self.assertEqual(max_integer([4, 2, 3, 1]), 4, "max at the beginning")
        self.assertEqual(max_integer([2, 3, 1]), 3, "max at the middle")
        self.assertEqual(max_integer([3]), 3, "list of one element")
        self.assertEqual(max_integer([]), None, "list is empty")

    def test_nigative_input(self):
        """testing for nigative number"""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4, "nigative number")
        self.assertEqual(max_integer([1, -2, 3, -4]), 3, "nigative number")
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1, "nigative number")


if __name__ == '__main__':
    unittest.main()
