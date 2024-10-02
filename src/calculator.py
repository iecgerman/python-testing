def sum(a,b):

    """
    # sesion interactiva
    >>> sum(5,7)
    12

    >>> sum(4,-4)
    0
    """

    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    """
    >>> divide(10,0)
    Traceback (most recent call last):
    ValueError: La division por cero no esta permitida
    """
    if b == 0:
        raise ValueError("La division por cero no esta permitida")
    return a / b