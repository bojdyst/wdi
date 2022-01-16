from zadanie_3 import is_prime_rec
from zadanie_3 import potegowanie 
import unittest
import pytest

class Testingmath(unittest.TestCase):
    def test_exponentation(self):
        self.assertEqual(potegowanie(5, 2), 25) 
    
    def test_prime(self):
        self.assertEqual(is_prime_rec(5), 1)

# def test_expon():
#     assert 49 == potegowanie(7, 2)

# def test_pri():
#     assert 1 == is_prime_rec(7)