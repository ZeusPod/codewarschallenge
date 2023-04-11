def get_middle(s):
    s = list(s)
    first = int(len(s)/2) - 1
    if len(s) % 2 == 0:
        result = slice(first, first + 2)
        return ''.join(s[result])
    else:
        return s[first +1]


print(get_middle('testing'))




