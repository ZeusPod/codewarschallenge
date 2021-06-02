import string

chars = ['a','b','c','d','f']

def find_missing_letter(chars):
    for index in range(len(chars) - 1):
        if ord(chars [index + 1]) - ord(chars[index]) != 1:
            return chr(ord(chars[index]) + 1)
    

my_find = find_missing_letter(chars)
print(my_find)