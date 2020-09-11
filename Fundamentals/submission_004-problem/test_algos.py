import unittest
from unittest.mock import patch
from io import StringIO
import super_algos


class TestAlgos(unittest.TestCase):

    def test_minimum_num(self):
        """Test Minimum Number in find_min"""

        codetest = super_algos.find_min([7, 2, 8, 5, 6])
        self.assertEqual(codetest, 2)


    def test_character_min(self):
        """Test a char in find_min"""

        codetest = super_algos.find_min([7, 2, 8, 5, 6, "a"])
        self.assertEqual(codetest, -1)
    

    def test_no_elements_min(self):
        """Test no elements in find_min"""

        codetest = super_algos.find_min([])
        self.assertEqual(codetest, -1)
    

    def test_single_element_min(self):
        """Test Single element in find_min"""

        codetest = super_algos.find_min([1])
        self.assertEqual(codetest, 1)
    

    def test_sum_digits(self):
        """Test sum digits in sum_all"""

        codetest = super_algos.sum_all([3, 4, 6, 8, 2])
        self.assertEqual(codetest, 23)


    def test_character_sum(self):
        """Test char in sum_all"""

        codetest = super_algos.sum_all([4, 5, 6, 3, "a"])
        self.assertEqual(codetest, -1)


    def test_no_elements_sum(self):
        """Test no elements in sum_all"""

        codetest = super_algos.sum_all([])
        self.assertEqual(codetest, -1)
    

    def test_string_combinations(self):
        """Test string combinations in find_possible_strings"""

        codetest = super_algos.find_possible_strings(["c", "d"], 3)
        self.assertEqual(['ccc', 'ccd', 'cdc', 'cdd', 'dcc', 'dcd', 'ddc', 'ddd'], codetest)


    def test_string_single(self):
        """Test string with n = 1 in find_possible_strings"""

        codetest = super_algos.find_possible_strings(["a", "b", "c"], 1)
        self.assertEqual(["a", "b", "c"], codetest)
    

    def test_string_integers(self):
        """Test integers in find_possible_strings"""

        codetest = super_algos.find_possible_strings(["a", "b", 1, 2], 2)
        self.assertEqual([], codetest)


    def test_string_blank(self):
        """Test blank string in find_possible_strings"""
        
        codetest = super_algos.find_possible_strings([], 2)
        self.assertEqual([],[])