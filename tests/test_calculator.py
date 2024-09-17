import unittest

from src.calculator import sum, subtract, multiply, divide

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        assert sum(2,3) == 5

    def test_subtract(self):
        assert subtract(10,5) == 5
    
    def test_multiply(self):
        assert multiply(3,2) == 6

    def test_divide(self):
        result = divide(10,2)
        expected = 5
        assert result == expected


# corremos el siguiente comando en la terminal:

# python -m unittest discover -s tests

# Resultado:

# (venv) PS C:\Users\info\python-testing\PYTHON-TESTING> python -m unittest discover -s tests
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s

# OK
# (venv) PS C:\Users\info\python-testing\PYTHON-TESTING> 