#!/usr/bin/python3
import unittest

class TestMaxInt(unittest.TestCase):

    def setUp(self):
        """setup the function"""
        self.max_integer = __import__('6-max_integer').max_integer

    def test_normal(self):
        self.assertEqual(self.max_integer([1, 2, 3, 4]), 4)
