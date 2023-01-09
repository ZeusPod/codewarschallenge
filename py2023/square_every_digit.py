"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
"""

def square_digits(num): 
    list_num = list(str(num))
    sqrt = [int(x)*int(x) for x in list_num ]
    result = [str(x) for x in sqrt]
    r = "".join(result)
    return int(r)

my_sqrt = square_digits(9119)
print(my_sqrt)


