import doctest

def get_count(setence):
    """
    >>> get_count('Hello World')
    3
    
    >>> get_count('bienvenidos a python')
    7
    """
    
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in setence:
        if c in vowels:
            count += 1
    return count


doctest.testmod()


