from collections import Counter
import doctest


def stray(arr:list)->int:
    """
    function to filter de unique number in a list
    
    >>> stray([5,5,5,5,5,2,1,1,1,1,])
    2
    >>> stray([1,2,1,2,3])
    3
    """

    numbers = Counter(arr)
    for k,v in numbers.items():
        if v == 1:
            return k


doctest.testmod()


