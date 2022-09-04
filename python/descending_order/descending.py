def descending_order(num):
    list_num = str(num)
    numbers = [] 
    [numbers.append(x) for x in list_num]
    numbers.sort()
    numbers.reverse()
    high = ''.join(numbers)
    return int(high)
    


print(descending_order(42145))
