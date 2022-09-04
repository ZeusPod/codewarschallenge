def find_mult_numbers(integer:int, limit:int)->list:
    numbers=[]
    for x in range(integer, limit + 1):
        if x % integer == 0:
            numbers.append(x)

    return numbers

print(find_mult_numbers(5,25))
