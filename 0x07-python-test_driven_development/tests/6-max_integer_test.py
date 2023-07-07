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
        """testing normal case"""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()
