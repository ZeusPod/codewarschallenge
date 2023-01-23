def digitize(n):
    numbers = str(n)
    list_numbers = list(numbers)
    result = [int(x) for x in list_numbers]
    return result[::-1]

print(digitize(541215112))
