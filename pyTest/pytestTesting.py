#Algoritmos para probar pytest.
def fibonnaci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonnaci(number-1)+fibonnaci(number-2)

def palindromo(sentence): 
    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]

def suma(*args): 
    return sum(args)

def factorial(number):
    if number == 0: return 1
    else: return number*factorial(number-1)