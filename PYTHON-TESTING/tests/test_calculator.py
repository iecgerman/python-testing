import unittest

from src.calculator import sum, subtract

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        assert sum(2,3) == 5

    def test_subtract(self):
        assert subtract(10,5) == 5
               


