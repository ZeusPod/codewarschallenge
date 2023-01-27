#(13) is the minimum number could be formed from {1, 3, 1} , Without duplications

def min_value(digits):
    values = set(digits)
    numbers =[str(x) for x in values]
    result = sorted(numbers)
    minimum = "".join(result)
    return int(minimum)
    
    
    


print(min_value([4, 8, 1, 4]))
