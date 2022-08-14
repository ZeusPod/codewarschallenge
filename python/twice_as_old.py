def twice_as_old(dad_years_old, son_years_old):
    result = dad_years_old - (son_years_old * 2) 
    if result < 0:
        return result * -1
    else:
        return result
