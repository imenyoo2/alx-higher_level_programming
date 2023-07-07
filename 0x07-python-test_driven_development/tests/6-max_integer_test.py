#!/usr/bin/python3
import unittest
"""test cases for max_integer function"""


class TestMaxInt(unittest.TestCase):
    """test case for max_integer"""
    def setUp(self):
        """setup the function"""
        self.max_integer = __import__('6-max_integer').max_integer

    def test_normal(self):
        """testing normal case"""
        self.assertEqual(self.max_integer([1, 2, 3, 4]), 4)
