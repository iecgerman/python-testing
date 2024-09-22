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

# Pasos:

# primero activamos el entorno virtual

# PS C:\Users\info\python-testing> .\venv\Scripts\activate   
# (venv) PS C:\Users\info\python-testing> 

# corremos el siguiente comando en la terminal:

# python -m unittest discover -s tests

# Resultado:

# (venv) PS C:\Users\info\python-testing> python -m unittest discover -s tests
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s

# OK
# (venv) PS C:\Users\info\python-testing>

