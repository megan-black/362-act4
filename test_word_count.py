import unittest
import pytest

def word_count(string):
    arr = string.split(' ')
    return len(arr)

#unittest class for wordcount testing
class TestCase(unittest.TestCase):
    def test_good(self):
        self.assertEqual(word_count('Hello world, nice to meet you'), 6)
    def test_list(self):
        self.assertRaises(AttributeError, word_count, ['hi','hello'])
    def test_excep(self):
        self.assertRaises(AttributeError, word_count, 1234)
    def test_bad_err(self):
        self.assertEqual(word_count(1234), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)