# create function take 2 arguments and return the sum of number between that numbers

def sum_of_range(a,b):
    result= 0
    if b <2:
        result = a + b
    else: 
        for i in range(a, b +1):
            result = result + i 

    return result


print(sum_of_range(-1,0))


