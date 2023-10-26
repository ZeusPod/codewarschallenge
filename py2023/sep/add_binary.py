def add_binary(a,b):
    result = a + b 
    binary = bin(result)
    str_bin = binary[2:]
    return str_bin


print(add_binary(5, 9))
