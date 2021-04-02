"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

"""



def fibonnaci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonnaci(number-1)+fibonnaci(number-2)

def palindromo(sentence): #Doc String
    """Devuelve verdadero si el parámetro es un palíndromo, en caso contrario retorna falso.
    sentence -- String o entero

    >>> palindromo("anita lava la tina")
    True
    >>> palindromo("121")
    True
    """
    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]

def suma(*args): #Doc String
    """Sumando

    >>> suma(10,20,60,10)
    100
    """
    
    return sum(args)

class Recursivo:
    def factorial(self, number):
        if number == 0: return 1
        else: return number*self.factorial(number-1)

if __name__=="__main__":
    import doctest
    doctest.testmod()
    doctest.testfile("test.txt")