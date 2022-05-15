import doctest

def number(bus_stops):
    """ >>> number([[10,0],[3,5],[5,8]])
    5
    >>> number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
    17 
    """

    large = len(bus_stops)
    up_bus = 0
    down = 0 
    for i in range(large):
        up_bus += bus_stops[i][0]
        down += bus_stops[i][1]
    return up_bus - down


doctest.testmod()    