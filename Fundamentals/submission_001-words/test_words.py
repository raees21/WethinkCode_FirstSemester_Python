import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import word_processor

class TestWords(unittest.TestCase):
    def test_convert_lower(self):
        self.assertEqual(word_processor.convert_to_word_list("HeLlo HoW aRe You"), ["hello", "how", "are", "you"])

    def test_convert_single_word(self):
        self.assertEqual(word_processor.convert_to_word_list("Hello"), ["hello"])

    def test_convert_none_string(self):
        self.assertEqual(word_processor.convert_to_word_list(""), [])

    def test_words_longer_than(self):
        self.assertEqual(word_processor.words_longer_than(4, "hello how Are you Doing"), ["hello", "doing"])

    def test_empty_longer_than(self):
        self.assertEqual(word_processor.words_longer_than(0, ""), [])

    def test_single__longer_than(self):
        self.assertEqual(word_processor.words_longer_than(1, "Hello"), ["hello"])

    def test_words_length_map(self):
        self.assertEqual(word_processor.words_lengths_map("Hello How are you doing today"), {3: 3, 5: 3})

    def test_single_length_map(self):
        self.assertEqual(word_processor.words_lengths_map("Hello"), {5: 1})

    def test_letter_map(self):
        self.assertEqual(word_processor.letters_count_map("hello how are you"), {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 2, 'f': 0, 'g': 0, 'h': 2, 'i': 0,
                                                                                 'j': 0, 'k': 0, 'l': 2, 'm': 0,'n': 0, 'o': 3, 'p': 0, 'q': 0, 'r': 1, 
                                                                                 's': 0, 't': 0, 'u': 1, 'v': 0, 'w': 1, 'x': 0, 'y': 1, 'z': 0})

    def test_letter_map_empty(self):
        self.assertEqual(word_processor.letters_count_map(""), {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
                                                                                 'j': 0, 'k': 0, 'l': 0, 'm': 0,'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 
                                                                                 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})

    def test_max_letter(self):
        self.assertEqual(word_processor.most_used_character("Hello"), 'l')

    def test_empty_max_letter(self):
        self.assertEqual(word_processor.most_used_character(""), None)