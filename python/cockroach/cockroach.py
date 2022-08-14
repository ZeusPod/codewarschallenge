# create a function take speed in km per hour and returns it in cm per seconds, rounded
# down to integer(=floored)

import doctest

def cockroach_speed(s):
    """
    >>> cockroach_speed(1.08)
    30
    """
    cms = 27.777777777778
    return round((int(s) * cms), 2)



doctest.testmod()
