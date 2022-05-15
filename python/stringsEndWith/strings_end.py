""" 
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). 
"""
import doctest


def solution(string: str, ending:str):
    """ 
    >>> solution('abcde','cde')
    True
    >>> solution('abcde','de')
    True
    >>> solution('abcde','')
    True
    """
    large = len(ending)
    if string[-(large):] == ending:
        
        return True
    elif ending == '':
        return True
    else: 
        return False



doctest.testmod()