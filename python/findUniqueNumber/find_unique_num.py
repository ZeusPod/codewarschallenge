import doctest


def find_uniq(arr):
    """ Fucntion for find te unique number in array
    >>> find_uniq([ 1, 1, 1, 2, 1, 1 ])
    2
    >>> find_uniq([ 1, 5, 1, 2, 1, 1, 5, 8, 2, 3, 8]) 
    3
    """
    numbers = {} 
    for i in arr:
        if i not in numbers:
            numbers[i] = 1 
        else:
            numbers[i] += 1

    for key, value in numbers.items():
        if value == 1:
            return key
    
doctest.testmod()