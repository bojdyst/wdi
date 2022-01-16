from zadanie_2_complex_numbers import sub
from zadanie_2_complex_numbers import add
import unittest
import pytest

class Testmath(unittest.TestCase):
    def test_adding(self):
        self.assertEqual(add(5+5j, 5+5j), 10+10j)

    def test_sub(self):
        self.assertEqual(sub(10+4j, 2-4j), 8+8j)

def test_add():
    assert 6+7j == add(3+3j, 3+4j)

def test_subt():
    assert 8-9j == sub(10-18j, 2-9j)