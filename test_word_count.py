import unittest
import pytest

def word_count(string):
    arr = string.split(' ')
    return len(arr)

# #unittest class for wordcount testing
# class TestCase(unittest.TestCase):
#     def test_good(self):
#         self.assertEqual(word_count('Hello world, nice to meet you'), 6)
#     def test_list(self):
#         self.assertRaises(AttributeError, word_count, ['hi','hello'])
#     def test_excep(self):
#         self.assertRaises(AttributeError, word_count, 1234)
#     def test_bad_err(self):
#         self.assertEqual(word_count(1234), 1)

# if __name__ == "__main__":
#     unittest.main(verbosity=2)

# # pytest class for word count testing       
# class TestClass:
#     def test_one(self):
#         assert word_count('hello world') == 2
#     def test_two(self):
#         assert word_count('') == 1
#     def test_three(self):
#         with pytest.raises(AttributeError):
#             assert word_count([1,2]) == 1
#     def test_four(self):
#         assert word_count(1) == AttributeError