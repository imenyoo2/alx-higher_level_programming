#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test case for max_integer"""

    def test_normal(self):
        """testing normal case"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_nigative_input(self):
        """testing for nigative number"""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_normal(self):
        """testing for max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "max at the end")


if __name__ == '__main__':
    unittest.main()
