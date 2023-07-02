from unittest import TestCase

from python_leetcode.validpalindrome125 import is_valid_palindrome


class TestIsValidPalindrome(TestCase):
    def test_is_valid_palindrome1(self):
        valid_palindrome = "A man, a plan, a canal: Panama"
        self.assertTrue(is_valid_palindrome(valid_palindrome), "A man, a plan, a canal: Panama")

    def test_is_valid_palindrome2(self):
        invalid_palindrome = ""
        self.assertFalse(is_valid_palindrome(invalid_palindrome), "{EMPTY STRING} ie \"\"")

    def test_is_valid_palindrome3(self):
        invalid_palindrome = " "
        self.assertFalse(is_valid_palindrome(invalid_palindrome), "{ONE SPACE} ie \" \" ")

    def test_is_valid_palindrome4(self):
        valid_palindrome = "A"
        self.assertTrue(is_valid_palindrome(valid_palindrome), "A")

    def test_is_valid_palindrome5(self):
        valid_palindrome = "aa"
        self.assertTrue(is_valid_palindrome(valid_palindrome), "aa")

    def test_is_valid_palindrome6(self):
        invalid_palindrome = "ab"
        self.assertFalse(is_valid_palindrome(invalid_palindrome), "ab")

    def test_is_valid_palindrome7(self):
        valid_palindrome = "AbBa"
        self.assertTrue(is_valid_palindrome(valid_palindrome), "AbBa")
