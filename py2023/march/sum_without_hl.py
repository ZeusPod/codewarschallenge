# function to sum element of array without lower and highest numbers 

def sum_array(arr):
    if len(arr) == 0 or len(arr) == None or arr == None:
        return 0
    else:
        numbers =  sorted(arr)
        numbers.pop(0)
        numbers.pop()
        return sum(numbers)

print(sum_array(None))


