def number(bus_stops):
    large = len(bus_stops)
    up_bus = 0
    down = 0 
    for i in range(large):
        up_bus += bus_stops[i][0]
        down += bus_stops[i][1]
    return up_bus - down


    