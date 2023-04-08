#!/usr/bin/python3
"""unittest for max_integer([..])
"""
import unittest
import sys

sys.path.insert(0, "../")
max_integer = __import__("6-max_integer").max_integer

class TestMaxIntegerFunction(unittest.TestCase):
    
    def test_output(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 5, 3, 1]), 5)

    def test_parameter_type(self):
        self.assertIsNone(max_integer("not list"))
    
    def test_return_type(self):
        self.assertIsInstance(max_integer([2, 3, 4]), int)
