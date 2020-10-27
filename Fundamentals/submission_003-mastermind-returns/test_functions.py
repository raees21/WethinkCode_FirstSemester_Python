import unittest
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests
import mastermind
from unittest.mock import patch


class TestMastermind(unittest.TestCase):
    """Test for Duplicate digits and range in create_code function"""

    def test_duplicate_range(self):
        for i in range(0, 100):
            codetest =  mastermind.create_code()
            self.assertEqual(len(codetest), 4)
            for j in range(0, 4):
                if codetest[j] < 1 or codetest[j] > 8:
                    self.assertFalse(codetest[j], "Code not in range 1 - 8")

      
    def test_true_false(self):
        """Test to see if the check_coorectness function returns True or False Correctly"""
        with captured_io(''):
            self.assertTrue(mastermind.check_correctness(1,4))
            self.assertFalse(mastermind.check_correctness(1, 3))
        

    def test_user_input(self):
        """Test user input using patch to see if it only allows 4 digits"""
        with captured_io(StringIO("123\n12345\n1234")):
            self.assertEqual(len(mastermind.get_answer_input()), 4)

        pass


    def test_digits(self):
        """Test user input using patch agaisnt the take_turn function to see if the
           correct digits in position and the correct digits alone are being recorded
           correctly"""
        
        code = [1, 2, 3, 4]

        with captured_io(StringIO("1234\n2341\n2134\n8734\n8743")):

            correct_digits = mastermind.take_turn(code)
            self.assertEqual((correct_digits[0], correct_digits[1]), (4, 0))

            correct_digits = mastermind.take_turn(code)
            self.assertEqual((correct_digits[0], correct_digits[1]), (0, 4))

            correct_digits = mastermind.take_turn(code)
            self.assertEqual((correct_digits[0], correct_digits[1]), (2, 2))

            correct_digits = mastermind.take_turn(code)
            self.assertEqual((correct_digits[0], correct_digits[1]), (2, 0))

            correct_digits = mastermind.take_turn(code)
            self.assertEqual((correct_digits[0], correct_digits[1]), (0, 2))