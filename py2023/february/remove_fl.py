def remove_char(s):
    string = list(s)
    string.pop()
    return "".join(string[1:])


print(remove_char('josemorales'))
