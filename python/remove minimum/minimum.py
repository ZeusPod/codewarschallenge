def remove_smallest(numbers):
    small = numbers.copy()
    small.sort()
    result = small[1:]
    return result


print(remove_smallest([5,1,3,5,6,7,2,4]))
