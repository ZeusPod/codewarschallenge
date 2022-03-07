def likes(names):
    """
    Function that returns a sentence describing the people who like an item.
    >>> likes(['Alex', 'Jacob', 'Mark', 'Max'])
    'Alex, Jacob and 2 others like this'
    >>> likes([])
    'no one likes this'
    
    """
    largest = len(names)
    if largest == 0:
        return "no one likes this"
    elif largest == 1:
        return f"{names[0]} likes this"
    elif largest == 2:
        return f"{names[0]} and {names[1]} like this"
    elif largest == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {largest - 2} others like this"
        
