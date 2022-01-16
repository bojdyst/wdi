from zadanie_6_prime_numbers import czy_jest_pierwszą
import unittest
import pytest

class TestCube(unittest.TestCase):
    def test_is_true(self):
        self.assertEqual(czy_jest_pierwszą(23), True)

    def test_is_int(self):
        self.assertRaises(TypeError, czy_jest_pierwszą(5), True)


def test_is_true():
    assert True == czy_jest_pierwszą(3)

def test_is_int():
        with pytest.raises(TypeError):      #działa na odwrót, błąd jak jest liczba, bo nie ma TypeError
            czy_jest_pierwszą()
