#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unittesting
    """
    def test_maxend(self):
        """
        Test for "max at the end" exists
        """
        self.assertEqual(max_integer([4, 3, 9]), 9)

    def test_maxbeginning(self):
        """
        Test for "max at the beginning" exists
        """
        self.assertEqual(max_integer([10, 4, 3, 9]), 10)

    def test_maxmiddle(self):
        """
        Test for "max at the beginning" exists
        """
        self.assertEqual(max_integer([10, 20, 9]), 20)

    def test_NegativeNumber(self):
        """
        Test for “one negative number in the list” exists
        """
        self.assertEqual(max_integer([10, 20, -9]), 20)

    def test_AllNegative(self):
        """
        or “only negative numbers in the list” exists
        """
        self.assertEqual(max_integer([-10, -20, -9]), -9)

    def test_OneElement(self):
        """
        Test for “list of one element” exists
        """
        self.assertEqual(max_integer([5]), 5)

    def test_EmptyList(self):
        """
        Test for “list of one element” exists
        """
        self.assertEqual(max_integer([]), None)
