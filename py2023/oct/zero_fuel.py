import doctest

def zero_fuel(distance_to_pump, mpg, fuel_left)->bool:
    """
        function for calculate if the mpg remaining 
        is enough to reach the pump 

        >>> zero_fuel(50,25,2)
        True
        >>> zero_fuel(100,50,1)
        False
    """
    return True if mpg * fuel_left >= distance_to_pump else False


if __name__ == "__main__":
    doctest.testmod()
