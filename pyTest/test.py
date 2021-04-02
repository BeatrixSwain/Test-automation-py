#Tests example
from pytestTesting import palindromo, suma, factorial, fibonnaci

def test_fibonacci_cinco():
    assert fibonnaci(5) == 5

def test_palindromo_anita():
    assert palindromo("Anita lava la tina")

def test_factorial_cinco():
    assert factorial(5)==120


