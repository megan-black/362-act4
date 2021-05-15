import unittest
import pytest

def pal(string):
    if(string == string[::-1]):
        return "The string is a palindrome"
    return "The string is not a palindrome"

#unittest class for palindrome testing
class TestCase(unittest.TestCase):
    def test_good_is(self):
        self.assertEqual(pal('racecar'), "The string is a palindrome")
    def test_good_isnt(self):
        self.assertEqual(pal('hello'), "The string is not a palindrome")
    def test_excep(self):
        self.assertRaises(TypeError, pal, 1234)
    def test_bad_err(self):
        self.assertEqual(pal(1234), "The string is not a palindrome")

if __name__ == "__main__":
    unittest.main(verbosity=2)

# pytest class for palindrome testing       
# class TestClass:
#     def test_one(self):
#         assert pal('asdfdsa') == "The string is a palindrome"
#     def test_two(self):
#         assert pal('hello') == "The string is not a palindrome"
#     def test_three(self):
#         assert pal('hi') == "The string is a palindrome"
#     def test_four(self):
#         assert pal(1) == "The string is a palindrome"
