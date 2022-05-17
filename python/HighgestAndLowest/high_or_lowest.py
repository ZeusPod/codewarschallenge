"""En esta pequeña tarea, se le da una cadena de números separados por espacios y tiene que devolver el número más alto y el más bajo.
Translated with Google (English → Spanish)"""
import doctest
from pydoc import doc

def high_and_low(numbers:str):
    """ fuction find low and high numbers  
    >>> high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
    '42 -9'
    """
    numbers = numbers.split(" ")
    numbers = [int(i) for i in numbers]
    numbers.sort()
    return str(numbers[-1]) + " " + str(numbers[0])


doctest.testmod()



