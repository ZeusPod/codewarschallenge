# given a array of intengers, return a new array with each value doubled.

import doctest
from re import I

def lostWithoutMap(arr):
    """ function to return a new arr with double of given array
    
    >>> lostWithoutMap([2,4,6,8])
    [4, 16, 36, 64]

    >>> lostWithoutMap([5,3,10])
    [25, 9, 100]
    """
    return list(map(lambda x: x*x, arr))
    
    
doctest.testmod()


